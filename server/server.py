from classes.dodo_classes import ToDo, Note, Profile, Tag, NoteTagRel
from classes import dodo_classes
from google.protobuf.timestamp_pb2 import Timestamp
from sqlalchemy import create_engine
from requirements.secrets_file import connection_credentials

import grpc
import time
import logging

import protobufs.dodo_servicer_pb2_grpc as rpc
import protobufs.dodo_servicer_pb2 as dodo


class Server(rpc.DoDoServicer):

    def __init__(self):
        self.connections = []
        self.engine = create_engine(connection_credentials)

    def InsertToDo(self, request, context):
        logging.info("New ToDo is going to be inserted.")
        todo = dodo_classes.convert_todo(request)
        dodo_classes.insert_db_object(todo, self.engine)
        # ToDo: adding return

    def UpdateToDo(self, request, context):
        logging.info("New ToDo is going to be updated.")
        # ToDo: adding return

    def DeleteToDo(self, request, context):
        logging.info("New ToDo is going to be deleted..")
        todo_id = request.tid
        dodo_classes.delete_db_object(todo_id, ToDo, self.engine)
        # ToDo: adding return

    def InsertNote(self, request, context):
        logging.info("New Note is going to be inserted into database.")
        note = dodo_classes.convert_note(request)
        dodo_classes.insert_db_object(note, self.engine)
        # ToDo: adding return

    def UpdateNote(self, request, context):
        logging.info("New Note is going to be inserted into database.")
        # ToDo: adding return

    def DeleteNote(self, request, context):
        logging.info("New Note is going to be inserted into database.")
        note_id = request.nid
        dodo_classes.delete_db_object(note_id, Note, self.engine)
        # ToDo: adding return
