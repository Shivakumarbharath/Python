import socket

s=socket.socket()#by default it is AF_INET and SOCK_STREAM

s.connect(('localhost',5000))

file=input("Enter the file name")
s.send(file.encode())
content=s.recv(1024)
print(content.decode())#decode is used while printing on terminal

s.close()