import socket

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(('127.0.0.1',65432))
response=soc.recv(1024)
print(response)
soc.close()