from classes.dodo_classes import ToDo, Note, Profile, Tag, NoteTagRel
from classes import dodo_classes
from google.protobuf.timestamp_pb2 import Timestamp
from sqlalchemy import create_engine
from requirements.secrets_file import connection_credentials
from concurrent import futures

import grpc
import time
import logging

import protobufs.dodo_servicer_pb2_grpc as rpc
import protobufs.dodo_servicer_pb2 as dodo


class Server(rpc.DoDoServicer):

    def __init__(self):
        self.connections = []
        self.engine = create_engine(connection_credentials)

    # ToDOs

    def InsertToDo(self, request, context):
        logging.info("New ToDo is going to be inserted")
        todo = dodo_classes.convert_todo(request)
        dodo_classes.insert_db_object(todo, self.engine)
        # ToDo: adding return

    def UpdateToDo(self, request, context):
        logging.info("A ToDo is going to be updated")
        # ToDo: adding return

    def DeleteToDo(self, request, context):
        logging.info("A ToDo is going to be deleted")
        todo_id = request.tid
        dodo_classes.delete_db_object(todo_id, ToDo, self.engine)
        # ToDo: adding return

    # Notes

    def InsertNote(self, request, context):
        logging.info("New Note is going to be inserted")
        note = dodo_classes.convert_note(request)
        dodo_classes.insert_db_object(note, self.engine)
        # ToDo: adding return

    def UpdateNote(self, request, context):
        logging.info("A Note is going to be updated")
        # ToDo: adding return

    def DeleteNote(self, request, context):
        logging.info("A Note is going to be deleted")
        note_id = request.nid
        dodo_classes.delete_db_object(note_id, Note, self.engine)
        # ToDo: adding return

    # Profiles

    def InsertProfile(self, request, context):
        logging.info("New Profile is going to be inserted")
        profile = dodo_classes.convert_profile(request)
        dodo_classes.insert_db_object(profile, self.engine)
        # ToDo: adding return

    def DeleteProfile(self, request, context):
        logging.info("A Profile is going to be deleted")
        profile_id = request.pid
        dodo_classes.delete_db_object(profile_id, Profile, self.engine)
        # ToDo: adding return

    # Tags

    def InsertTag(self, request, context):
        logging.info("New Tag is going to be inserted")
        tag = dodo_classes.convert_tag(request)
        dodo_classes.insert_db_object(tag, self.engine)
        # ToDo: adding return

    def DeleteTag(self, request, context):
        logging.info("A Tag is going to be deleted")
        tag_id = request.taid
        dodo_classes.delete_db_object(tag_id, Tag, self.engine)
        # ToDo: adding return

    # NoteTagRel

    def InsertNoteTagRel(self, request, context):
        logging.info("New NotTagRel is going to be inserted")
        note_tag_rel = dodo_classes.convert_note_tag_rel(request)
        dodo_classes.insert_db_object(note_tag_rel, self.engine)
        # ToDo: adding return

    def DeleteNoteTagRel(self, request, context):
        logging.info("A NoteTagRel is going to be deleted")
        # ToDo: primary consists of two columns -> new delete process needed
        # ToDo: adding return


if __name__ == "__main__":
    print("Starting server...\n")
    port = 32002
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=16))
    rpc.add_DoDoServicer_to_server(Server(), server)
    server.add_insecure_port(f'0.0.0.0:{port}')
    server.start()
    server.wait_for_termination()
