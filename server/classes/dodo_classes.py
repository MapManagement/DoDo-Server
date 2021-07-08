import sys
import logging
from classes.database import DbConverter


sys.path.append("..")
from requirements.secrets_file import connection_credentials
import protobufs.dodo_servicer_pb2 as proto

from sqlalchemy import *
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
            creationDate=DbConverter.db_datetime_to_proto(self.creation_date)
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
            creationDate=DbConverter.db_datetime_to_proto(self.creation_date)
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


def generate_tables():
    db_engine = ""  # add your engine here
    Base.metadata.create_all(db_engine)
