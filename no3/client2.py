import socket

addr = ('localhost', 5000)
#addr = input("enter ip addr : ")
#port = input("enter port : ")
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#tes = (addr, int(port))
c.connect(addr)
count=0
data=input("input data : ")
extr=".txt"
judulasli=str(data)
judul=judulasli+extr
f = open(judul,'rb')
while f:
    if count==0:
        c.send(judulasli.encode())
        print(data)
    else:
        if not data:
            break
        c.send(data)
    data = f.read(1024)
    count = count+1
f.close()
c.close()