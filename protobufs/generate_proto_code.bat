echo Generating Python code...
python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. dodo_servicer.proto
echo Successfully generated Python code!