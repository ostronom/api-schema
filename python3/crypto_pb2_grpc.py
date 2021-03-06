# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import crypto_pb2 as crypto__pb2


class CryptoStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.KeyExchange = channel.unary_unary(
        '/dialog.Crypto/KeyExchange',
        request_serializer=crypto__pb2.RequestKeyExchange.SerializeToString,
        response_deserializer=crypto__pb2.ResponseKeyExchange.FromString,
        )


class CryptoServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def KeyExchange(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CryptoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'KeyExchange': grpc.unary_unary_rpc_method_handler(
          servicer.KeyExchange,
          request_deserializer=crypto__pb2.RequestKeyExchange.FromString,
          response_serializer=crypto__pb2.ResponseKeyExchange.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dialog.Crypto', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
