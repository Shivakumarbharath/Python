import socket

s=socket.socket()#by default it is AF_INET and SOCK_STREAM

s.connect(('localhost',4000))

# msg=s.recv(1024)
# print(msg.decode())

msg = s.recv(1024)
print(msg.decode())
#How many times  s.send is used that many times the s.ecieve is to be used
msg = s.recv(1024)
print(msg.decode())

s.close()