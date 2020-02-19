import socket
import sys
from datetime import datetime


addr = ('localhost', 5000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(1)
count=0
client, client_addr = s.accept()
while True:
    if count==0:
        data = client.recv(1024).decode()   
        cpy="_copy.txt"
        judul=str(data)+cpy
        f = open(judul,'wb')
    else:
        data = client.recv(1024)
        if not data:
            break
        f.write(data)
    count=count+1

f.close()

client.close()
s.close()


