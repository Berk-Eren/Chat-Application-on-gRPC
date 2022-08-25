C:\Users\BERKERE\.virtualenvs\grpc\Scripts\activate.exe;

set protos[0]="message";
set protos[1]="message_status";
set protos[2]="service";


(for %protoName in (%protos%) do (
   python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/message.proto
))

deactivate