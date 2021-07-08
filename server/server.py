from classes.dodo_classes import ToDo, Note, Profile, Tag, NoteTagRel, connection_error, DbManager
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
        self.db_manager = DbManager()

    # ToDOs --------------------------------------------------------------

    @connection_error
    def InsertToDo(self, request, context):
        logging.info("New ToDo is going to be inserted")
        todo = dodo_classes.convert_todo(request)
        self.db_manager.insert_db_object(todo)

    @connection_error
    def UpdateToDo(self, request, context):
        logging.info("A ToDo is going to be updated")
        todo_id = request.tid
        db_todo = self.db_manager.query_db_object([todo_id], ["t_id"], ToDo)
        db_todo.text = request.text
        db_todo.is_done = request.isDone
        db_todo.color = request.color

    @connection_error
    def DeleteToDo(self, request, context):
        logging.info("A ToDo is going to be deleted")
        todo_id = request.tid
        db_todo = self.db_manager.query_db_object([todo_id], ["t_id"], ToDo)
        self.db_manager.delete_db_object(db_todo)

    # Notes --------------------------------------------------------------

    @connection_error
    def InsertNote(self, request, context):
        logging.info("New Note is going to be inserted")
        note = dodo_classes.convert_note(request)
        self.db_manager.insert_db_object(note)

    @connection_error
    def UpdateNote(self, request, context):
        logging.info("A Note is going to be updated")
        note_id = request.nid
        db_note = self.db_manager.query_db_object([note_id], ["n_id"], Note)
        db_note.title = request.title
        db_note.content = request.content
        db_note.is_visible = request.isVisible
        db_note.is_highlighted = request.isHighlighted
        db_note.color = request.color

    @connection_error
    def DeleteNote(self, request, context):
        logging.info("A Note is going to be deleted")
        note_id = request.nid
        db_note = self.db_manager.query_db_object([note_id], ["n_id"], Note)
        self.db_manager.delete_db_object(db_note)

    # Profiles --------------------------------------------------------------

    @connection_error
    def InsertProfile(self, request, context):
        logging.info("New Profile is going to be inserted")
        profile = dodo_classes.convert_profile(request)
        self.db_manager.insert_db_object(profile)

    @connection_error
    def DeleteProfile(self, request, context):
        logging.info("A Profile is going to be deleted")
        profile_id = request.pid
        db_profile = self.db_manager.query_db_object([profile_id], ["p_id"], Profile)
        self.db_manager.delete_db_object(db_profile)

    # Tags --------------------------------------------------------------

    @connection_error
    def InsertTag(self, request, context):
        logging.info("New Tag is going to be inserted")
        tag = dodo_classes.convert_tag(request)
        self.db_manager.insert_db_object(tag)

    @connection_error
    def DeleteTag(self, request, context):
        logging.info("A Tag is going to be deleted")
        tag_id = request.taid
        tag = self.db_manager.query_db_object([tag_id], ["ta_id"], Tag)
        self.db_manager.delete_db_object(tag)

    # NoteTagRel --------------------------------------------------------------

    @connection_error
    def InsertNoteTagRel(self, request, context):
        logging.info("New NotTagRel is going to be inserted")
        note_tag_rel = dodo_classes.convert_note_tag_rel(request)
        self.db_manager.insert_db_object(note_tag_rel)

    @connection_error
    def DeleteNoteTagRel(self, request, context):
        logging.info("A NoteTagRel is going to be deleted")
        note_tag_rel_ids = [request.nid, request.tid]
        note_tag_rel = self.db_manager.query_db_object(note_tag_rel_ids, ["n_id", "t_id"], NoteTagRel)
        self.db_manager.delete_db_object(note_tag_rel)


if __name__ == "__main__":
    print("Starting server...\n")
    port = 32002
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=16))
    rpc.add_DoDoServicer_to_server(Server(), server)
    server.add_insecure_port(f'0.0.0.0:{port}')
    server.start()
    server.wait_for_termination()
