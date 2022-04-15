import nacl.utils
import socket

def aleatorio():
    a=nacl.utils.random(128)
    print(len(a))
    x=''
    for i in range(len(a)):
        x+="%02x " % (a[i])
    return x

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(('127.0.0.1',65432))
soc.listen()
x,ad=soc.accept()
print(f'{ad} conectado')
aleatorioo=aleatorio().encode()
print(f'se envia aleatorio: {aleatorioo}')
x.sendall(aleatorioo)
x.close()
soc.close()