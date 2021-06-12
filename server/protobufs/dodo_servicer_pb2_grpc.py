# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protobufs.dodo_servicer_pb2 as dodo__servicer__pb2


class DoDoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InsertToDo = channel.unary_unary(
                '/grpc.DoDo/InsertToDo',
                request_serializer=dodo__servicer__pb2.ToDo.SerializeToString,
                response_deserializer=dodo__servicer__pb2.SuccessResponse.FromString,
                )
        self.UpdateToDo = channel.unary_unary(
                '/grpc.DoDo/UpdateToDo',
                request_serializer=dodo__servicer__pb2.ToDo.SerializeToString,
                response_deserializer=dodo__servicer__pb2.SuccessResponse.FromString,
                )
        self.DeleteToDo = channel.unary_unary(
                '/grpc.DoDo/DeleteToDo',
                request_serializer=dodo__servicer__pb2.ToDoIdentifier.SerializeToString,
                response_deserializer=dodo__servicer__pb2.SuccessResponse.FromString,
                )
        self.InsertNote = channel.unary_unary(
                '/grpc.DoDo/InsertNote',
                request_serializer=dodo__servicer__pb2.Note.SerializeToString,
                response_deserializer=dodo__servicer__pb2.SuccessResponse.FromString,
                )
        self.UpdateNote = channel.unary_unary(
                '/grpc.DoDo/UpdateNote',
                request_serializer=dodo__servicer__pb2.Note.SerializeToString,
                response_deserializer=dodo__servicer__pb2.SuccessResponse.FromString,
                )
        self.DeleteNote = channel.unary_unary(
                '/grpc.DoDo/DeleteNote',
                request_serializer=dodo__servicer__pb2.NoteIdentifier.SerializeToString,
                response_deserializer=dodo__servicer__pb2.SuccessResponse.FromString,
                )
        self.InsertProfile = channel.unary_unary(
                '/grpc.DoDo/InsertProfile',
                request_serializer=dodo__servicer__pb2.Profile.SerializeToString,
                response_deserializer=dodo__servicer__pb2.SuccessResponse.FromString,
                )
        self.DeleteProfile = channel.unary_unary(
                '/grpc.DoDo/DeleteProfile',
                request_serializer=dodo__servicer__pb2.Profile.SerializeToString,
                response_deserializer=dodo__servicer__pb2.SuccessResponse.FromString,
                )
        self.InsertTag = channel.unary_unary(
                '/grpc.DoDo/InsertTag',
                request_serializer=dodo__servicer__pb2.Tag.SerializeToString,
                response_deserializer=dodo__servicer__pb2.SuccessResponse.FromString,
                )
        self.DeleteTag = channel.unary_unary(
                '/grpc.DoDo/DeleteTag',
                request_serializer=dodo__servicer__pb2.Tag.SerializeToString,
                response_deserializer=dodo__servicer__pb2.SuccessResponse.FromString,
                )
        self.InsertNoteTagRel = channel.unary_unary(
                '/grpc.DoDo/InsertNoteTagRel',
                request_serializer=dodo__servicer__pb2.NoteTagRel.SerializeToString,
                response_deserializer=dodo__servicer__pb2.SuccessResponse.FromString,
                )
        self.DeleteNoteTagRel = channel.unary_unary(
                '/grpc.DoDo/DeleteNoteTagRel',
                request_serializer=dodo__servicer__pb2.NoteTagRel.SerializeToString,
                response_deserializer=dodo__servicer__pb2.SuccessResponse.FromString,
                )


class DoDoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InsertToDo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateToDo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteToDo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertTag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertNoteTagRel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNoteTagRel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DoDoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InsertToDo': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertToDo,
                    request_deserializer=dodo__servicer__pb2.ToDo.FromString,
                    response_serializer=dodo__servicer__pb2.SuccessResponse.SerializeToString,
            ),
            'UpdateToDo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateToDo,
                    request_deserializer=dodo__servicer__pb2.ToDo.FromString,
                    response_serializer=dodo__servicer__pb2.SuccessResponse.SerializeToString,
            ),
            'DeleteToDo': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteToDo,
                    request_deserializer=dodo__servicer__pb2.ToDoIdentifier.FromString,
                    response_serializer=dodo__servicer__pb2.SuccessResponse.SerializeToString,
            ),
            'InsertNote': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertNote,
                    request_deserializer=dodo__servicer__pb2.Note.FromString,
                    response_serializer=dodo__servicer__pb2.SuccessResponse.SerializeToString,
            ),
            'UpdateNote': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNote,
                    request_deserializer=dodo__servicer__pb2.Note.FromString,
                    response_serializer=dodo__servicer__pb2.SuccessResponse.SerializeToString,
            ),
            'DeleteNote': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNote,
                    request_deserializer=dodo__servicer__pb2.NoteIdentifier.FromString,
                    response_serializer=dodo__servicer__pb2.SuccessResponse.SerializeToString,
            ),
            'InsertProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertProfile,
                    request_deserializer=dodo__servicer__pb2.Profile.FromString,
                    response_serializer=dodo__servicer__pb2.SuccessResponse.SerializeToString,
            ),
            'DeleteProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProfile,
                    request_deserializer=dodo__servicer__pb2.Profile.FromString,
                    response_serializer=dodo__servicer__pb2.SuccessResponse.SerializeToString,
            ),
            'InsertTag': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertTag,
                    request_deserializer=dodo__servicer__pb2.Tag.FromString,
                    response_serializer=dodo__servicer__pb2.SuccessResponse.SerializeToString,
            ),
            'DeleteTag': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTag,
                    request_deserializer=dodo__servicer__pb2.Tag.FromString,
                    response_serializer=dodo__servicer__pb2.SuccessResponse.SerializeToString,
            ),
            'InsertNoteTagRel': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertNoteTagRel,
                    request_deserializer=dodo__servicer__pb2.NoteTagRel.FromString,
                    response_serializer=dodo__servicer__pb2.SuccessResponse.SerializeToString,
            ),
            'DeleteNoteTagRel': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNoteTagRel,
                    request_deserializer=dodo__servicer__pb2.NoteTagRel.FromString,
                    response_serializer=dodo__servicer__pb2.SuccessResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.DoDo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DoDo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def InsertToDo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DoDo/InsertToDo',
            dodo__servicer__pb2.ToDo.SerializeToString,
            dodo__servicer__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateToDo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DoDo/UpdateToDo',
            dodo__servicer__pb2.ToDo.SerializeToString,
            dodo__servicer__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteToDo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DoDo/DeleteToDo',
            dodo__servicer__pb2.ToDoIdentifier.SerializeToString,
            dodo__servicer__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsertNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DoDo/InsertNote',
            dodo__servicer__pb2.Note.SerializeToString,
            dodo__servicer__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DoDo/UpdateNote',
            dodo__servicer__pb2.Note.SerializeToString,
            dodo__servicer__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DoDo/DeleteNote',
            dodo__servicer__pb2.NoteIdentifier.SerializeToString,
            dodo__servicer__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsertProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DoDo/InsertProfile',
            dodo__servicer__pb2.Profile.SerializeToString,
            dodo__servicer__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DoDo/DeleteProfile',
            dodo__servicer__pb2.Profile.SerializeToString,
            dodo__servicer__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsertTag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DoDo/InsertTag',
            dodo__servicer__pb2.Tag.SerializeToString,
            dodo__servicer__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DoDo/DeleteTag',
            dodo__servicer__pb2.Tag.SerializeToString,
            dodo__servicer__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsertNoteTagRel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DoDo/InsertNoteTagRel',
            dodo__servicer__pb2.NoteTagRel.SerializeToString,
            dodo__servicer__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteNoteTagRel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.DoDo/DeleteNoteTagRel',
            dodo__servicer__pb2.NoteTagRel.SerializeToString,
            dodo__servicer__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
