"""Herd gRPC client library."""
import grpc
from typing import Optional
from proto import keyvaluestore_pb2 as herd_serv
from proto import keyvaluestore_pb2_grpc as herd_grpc

class HerdClient:
    """Client for the Herd gRPC service."""
    
    def __init__(self, host: str = 'localhost', port: int = 50051):
        """Initialize the client with host and port."""
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = herd_grpc.KeyValueServiceStub(self.channel)
    
    def set(self, key: str, value: bytes) -> bool:
        """Set a key-value pair."""
        request = herd_serv.SetRequest(key=key, value=value)
        response = self.stub.Set(request)
        return response.success
    
    def get(self, key: str) -> Optional[bytes]:
        """Get value by key."""
        request = herd_serv.GetRequest(key=key)
        response = self.stub.Get(request)
        return response.value if response.exists else None
    
    def delete(self, key: str) -> bool:
        """Delete a key-value pair."""
        request = herd_serv.DeleteRequest(key=key)
        response = self.stub.Delete(request)
        return response.success
    
    def close(self):
        """Close the gRPC channel."""
        self.channel.close()