import socket

#addr = ('localhost', 5000)
addr = input("enter ip addr : ")
port = input("enter port : ")
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tes = (addr, int(port))
c.connect(tes)
data=input("input data : ")
c.send(data.encode())
terima=c.recv(1024).decode()
print(terima)
c.close()