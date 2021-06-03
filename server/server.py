from classes.dodo_classes import ToDo, Note, Profile, Tag, NoteTagRel
from google.protobuf.timestamp_pb2 import Timestamp

import grpc
import time

import protobufs.dodo_servicer_pb2_grpc as rpc
import protobufs.dodo_servicer_pb2 as dodo


class Server(rpc.DoDoServicer):

    def __init__(self):
        self.connections = []
