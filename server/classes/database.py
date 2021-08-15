from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from requirements.secrets_file import connection_credentials
from dodo_classes import ToDo, Note, Profile, Tag, NoteTagRel

import datetime
import protobufs.dodo_servicer_pb2 as proto


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


class DbConverter:

    @staticmethod
    def convert_todo(proto_todo: proto.ToDo) -> ToDo:
        dodo_todo = ToDo(
            t_id=proto_todo.tid,
            creator_id=proto_todo.creatorID,
            text=proto_todo.text,
            color=proto_todo.color,
            is_done=proto_todo.isDOne
        )
        return dodo_todo

    @staticmethod
    def convert_note(proto_note: proto.Note) -> Note:
        dodo_note = Note(
            n_id=proto_note.nid,
            creator_id=proto_note.creatorID,
            title=proto_note.title,
            content=proto_note.content,
            color=proto_note.color,
            is_visible=proto_note.isVisible,
            is_highlighted=proto_note.isHighlighted,
            creation_date=str(proto_note.creationDate)
        )
        return dodo_note

    @staticmethod
    def convert_profile(proto_profile: proto.Profile) -> Profile:
        dodo_profile = Profile(
            p_id=proto_profile.pid,
            name=proto_profile.name,
            creation_date=str(proto_profile.creationdDate)
        )
        return dodo_profile

    @staticmethod
    def convert_tag(proto_tag: proto.Tag) -> Tag:
        dodo_tag = Tag(
            ta_id=proto_tag.taid,
            name=proto_tag.name
        )
        return dodo_tag

    @staticmethod
    def convert_note_tag_rel(proto_note_tag_rel: proto.NoteTagRel) -> NoteTagRel:
        dodo_note_tag_rel = NoteTagRel(
            nid=proto_note_tag_rel.nid,
            taid=proto_note_tag_rel.taid
        )
        return dodo_note_tag_rel

