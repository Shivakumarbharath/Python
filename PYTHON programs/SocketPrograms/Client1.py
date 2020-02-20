import socket

c=socket.socket()

c.connect(('localhost',9999))

c.send(bytes("Welcome To Sockets","utf-8"))

name=input('What is your name')

age=input('What is your age?')

c.send(bytes(name,'utf-8'))

c.send(bytes(age,'utf-8'))


print('Your Year Of Birth is ', int(c.recv(1024).decode()))