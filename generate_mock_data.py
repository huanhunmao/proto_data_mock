import sys
import subprocess
import json
import random
import string
from google.protobuf import descriptor_pb2
from google.protobuf.json_format import MessageToDict

def compile_proto(proto_path, output_path):
    """Compile the .proto file to generate descriptor file."""
    protoc_command = [
        'protoc',
        '--descriptor_set_out=' + output_path,
        '--include_imports',
        proto_path
    ]
    subprocess.run(protoc_command, check=True)

def read_descriptor_file(descriptor_path):
    """Read and parse the descriptor file."""
    with open(descriptor_path, 'rb') as f:
        file_descriptor_set = descriptor_pb2.FileDescriptorSet()
        file_descriptor_set.ParseFromString(f.read())
    return file_descriptor_set

def generate_mock_data(file_descriptor_set):
    mock_data = {}

    for file_descriptor in file_descriptor_set.file:
        for service in file_descriptor.service:
            for method in service.method:
                request_type = method.input_type.split(".")[-1]
                response_type = method.output_type.split(".")[-1]

                request_example = generate_example(file_descriptor, request_type)
                response_example = generate_example(file_descriptor, response_type)

                mock_data[method.name] = {
                    "request": request_example,
                    "response": response_example
                }
    return mock_data

def generate_example(file_descriptor, message_type):
    for message in file_descriptor.message_type:
        if (message.name == message_type):
            example = {}
            for field in message.field:
                example[field.name] = get_field_example(field)
            return example
    return {}

def get_field_example(field):
    if field.label == descriptor_pb2.FieldDescriptorProto.LABEL_REPEATED:
        return [get_field_example_single(field)] if field.type != descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE else []
    else:
        return get_field_example_single(field)

def get_field_example_single(field):
    field_type_example_map = {
        descriptor_pb2.FieldDescriptorProto.TYPE_DOUBLE: random.uniform(0, 100),
        descriptor_pb2.FieldDescriptorProto.TYPE_FLOAT: random.uniform(0, 100),
        descriptor_pb2.FieldDescriptorProto.TYPE_INT64: random.randint(0, 100),
        descriptor_pb2.FieldDescriptorProto.TYPE_UINT64: random.randint(0, 100),
        descriptor_pb2.FieldDescriptorProto.TYPE_INT32: random.randint(0, 100),
        descriptor_pb2.FieldDescriptorProto.TYPE_FIXED64: random.randint(0, 100),
        descriptor_pb2.FieldDescriptorProto.TYPE_FIXED32: random.randint(0, 100),
        descriptor_pb2.FieldDescriptorProto.TYPE_BOOL: random.choice([True, False]),
        descriptor_pb2.FieldDescriptorProto.TYPE_STRING: random_string(),
        descriptor_pb2.FieldDescriptorProto.TYPE_BYTES: random_bytes(),
        descriptor_pb2.FieldDescriptorProto.TYPE_UINT32: random.randint(0, 100),
        descriptor_pb2.FieldDescriptorProto.TYPE_ENUM: random.randint(0, 100),
        descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE: {}
    }
    return field_type_example_map.get(field.type, None)

def random_string(length=10):
    """Generate a random string."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_bytes(length=10):
    """Generate a random byte string."""
    return bytes(random.randint(0, 255) for _ in range(length))

if __name__ == "__main__":
    proto_file_path = sys.argv[1]
    descriptor_file_path = 'temp_descriptor.pb'

    compile_proto(proto_file_path, descriptor_file_path)

    file_descriptor_set = read_descriptor_file(descriptor_file_path)
    mock_data = generate_mock_data(file_descriptor_set)

    print(json.dumps(mock_data, indent=4))