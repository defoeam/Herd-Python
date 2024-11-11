import grpc
import keyvaluestore_pb2 as herd
import keyvaluestore_pb2_grpc as herd_grpc

def run():
    # Create a channel to the server
    channel = grpc.insecure_channel('localhost:50051')
    stub = herd_grpc.KeyValueServiceStub(channel)

    # Example: Set a key-value pair
    set_request = herd.SetRequest(key='0', value=b"example_value")
    set_response = stub.Set(set_request)
    print(f'Set Response: {set_response}')

    # Example: Get a value by key
    get_request = herd.GetRequest(key='0')
    get_response = stub.Get(get_request)
    print(f'Get Response: {get_response}')

    # Example: Delete a key-value pair
    delete_request = herd.DeleteRequest(key='0')
    delete_response = stub.Delete(delete_request)
    print(f'Delete Response: {delete_response}')

if __name__ == '__main__':
    run()