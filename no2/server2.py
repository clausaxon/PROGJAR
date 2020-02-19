import socket
import sys
from datetime import datetime


addr = ('localhost', 5000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
i=0
s.listen(5)
while True:
    datetimeObj = str(datetime.now())
    client, client_addr = s.accept()
    data = client.recv(1024).decode()


    tes = str(client_addr)
    timestampp = ("timestamp : "+datetimeObj+"\n informasi koneksi : "+tes+"\n pesan yang diterima : "+str(data)+"\n")
    f= open("logasli.txt","a")
    f.write(timestampp)
    print(timestampp)
    f.close()
    if data=="asklog":
        filename='logasli.txt'
        f = open(filename,'rb')
        all=f.read()
        client.send(str(all).encode())
        client.close()
    else :    
        datakirim=datetimeObj+tes+data
        client.send(datakirim.encode())
        client.close()        
    i=i+1
    if i==5:
        s.close()
        sys.exit(0)

