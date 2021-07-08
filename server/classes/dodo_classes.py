import datetime
import sys
import logging

import sqlalchemy.orm

sys.path.append("..")
from requirements.secrets_file import connection_credentials
import protobufs.dodo_servicer_pb2 as proto

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column

Base = declarative_base()


class ToDo(Base):
    __tablename__ = "todos"
    t_id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey("profiles.p_id"), nullable=False)
    text = Column(String(64), nullable=False)
    is_done = Column(Boolean, nullable=False)
    color = Column(String(7), default="#8e47d1")

    def __init__(self, t_id, creator_id, text, color, is_done):
        self.t_id = t_id
        self.creator_id = creator_id
        self.text = text
        self.color = color
        self.is_done = is_done

    def to_proto(self) -> proto.ToDo:
        proto_todo = proto.ToDo(
            tid=self.t_id,
            creatorID=self.creator_id,
            text=self.text,
            isDone=self.is_done,
            color=self.color
        )
        return proto_todo


class Note(Base):
    __tablename__ = "notes"
    n_id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey("profiles.p_id"), nullable=False)
    title = Column(String(32))
    content = Column(String(2048))
    creation_date = Column(DateTime, nullable=False)
    is_visible = Column(Boolean, nullable=False)
    is_highlighted = Column(Boolean, nullable=False)
    color = Column(String(7), default="#8e47d1")

    def __init__(self, n_id, creator_id, title, content, color, is_visible, is_highlighted, creation_date):
        self.n_id = n_id
        self.creator_id = creator_id
        self.title = title
        self.content = content
        self.creation_date = creation_date
        self.is_visible = is_visible
        self.is_highlighted = is_highlighted
        self.color = color

    def to_proto(self) -> proto.Note:
        proto_note = proto.Note(
            nid=self.n_id,
            creatorID=self.creator_id,
            title=self.title,
            content=self.content,
            isVisible=self.is_visible,
            isHighlighted=self.is_highlighted,
            color=self.color,
            creationDate=db_datetime_to_proto(self.creation_date)
        )
        return proto_note


class Profile(Base):
    __tablename__ = "profiles"
    p_id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    password = Column(String(256), nullable=false)
    creation_date = Column(DATETIME, nullable=False)

    def __init__(self, p_id, name, creation_date):
        self.p_id = p_id
        self.name = name
        self.creation_date = creation_date

    def to_proto(self) -> proto.Profile:
        proto_profile = proto.Profile(
            pid=self.p_id,
            name=self.name,
            creationDate=db_datetime_to_proto(self.creation_date)
        )
        return proto_profile


class Tag(Base):
    __tablename__ = "tags"
    ta_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(16), nullable=False)

    def __init__(self, ta_id, name):
        self.ta_id = ta_id
        self.name = name

    def to_proto(self) -> proto.Tag:
        proto_tag = proto.Tag(
            pid=self.ta_id,
            name=self.name,
        )
        return proto_tag


class NoteTagRel(Base):
    __tablename__ = "note_tag_rel"
    n_id = Column(Integer, ForeignKey("notes.n_id"), primary_key=True, nullable=False)
    ta_id = Column(Integer, ForeignKey("tags.ta_id"), primary_key=True, nullable=False)


def convert_todo(proto_todo: proto.ToDo) -> ToDo:
    dodo_todo = ToDo(
        t_id=proto_todo.tid,
        creator_id=proto_todo.creatorID,
        text=proto_todo.text,
        color=proto_todo.color,
        is_done=proto_todo.isDOne
    )
    return dodo_todo


def convert_note(proto_note: proto.Note) -> Note:
    dodo_note = Note(
        n_id=proto_note.nid,
        creator_id=proto_note.creatorID,
        title=proto_note.title,
        content=proto_note.content,
        color=proto_note.color,
        is_visible=proto_note.isVisible,
        is_highlighted=proto_note.isHighlighted,
        creation_date=proto_datetime_to_db(proto_note.creationDate)
    )
    return dodo_note


def convert_profile(proto_profile: proto.Profile) -> Profile:
    dodo_profile = Profile(
        p_id=proto_profile.pid,
        name=proto_profile.name,
        creation_date=proto_datetime_to_db(proto_profile.creationdDate)
    )
    return dodo_profile


def convert_tag(proto_tag: proto.Tag) -> Tag:
    dodo_tag = Tag(
        ta_id=proto_tag.taid,
        name=proto_tag.name
    )
    return dodo_tag


def convert_note_tag_rel(proto_note_tag_rel: proto.NoteTagRel) -> NoteTagRel:
    dodo_note_tag_rel = NoteTagRel(
        nid=proto_note_tag_rel.nid,
        taid=proto_note_tag_rel.taid
    )
    return dodo_note_tag_rel


def db_datetime_to_proto(db_datetime: DateTime) -> proto.DateTime:
    python_datetime = db_datetime.python_type
    proto_datetime = proto.DateTime(
        year=python_datetime.year,
        month=python_datetime.month,
        day=python_datetime.day,
        hour=python_datetime.hour,
        minute=python_datetime.minute,
        second=python_datetime.second
    )
    return proto_datetime


def proto_datetime_to_db(proto_date: proto.DateTime) -> DateTime:
    db_datetime = datetime.datetime(
        year=proto_date.year,
        month=proto_date.month,
        day=proto_date.day,
        hour=proto_date.hour,
        minute=proto_date.minute,
        second=proto_date.second
    )
    return db_datetime


class DbManager:

    def __init__(self):
        self.engine = create_engine(connection_credentials)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def insert_db_object(self, dodo_object):
        self.session.add(dodo_object)
        self.session.commit()

    def delete_db_object(self, db_object):
        self.session.delete(db_object)
        self.session.commit()

    def query_db_object(self, object_ids: list, field_names: list, object_type: type):
        conditions = {}
        for (object_id, field_name) in (object_ids, field_names):
            conditions.update({field_name: object_id})
        db_object = self.session.query(object_type).get(conditions)  # ToDo: needs to be tested
        return db_object


def connection_error(function: func):
    def wrapper(*args, **kwargs):
        try:
            function(*args, **kwargs)
            return proto.SuccessResponse(success=True)
        except Exception as ex:
            logging.error(f"Something went wrong while connecting to the client:\n"
                          f"{ex}")
            return proto.SuccessResponse(success=False)
    return wrapper


def generate_tables():
    Base.metadata.create_all(engine)
