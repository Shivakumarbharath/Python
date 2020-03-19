import socket

s = socket.socket()
print("Socket Created")

s.bind(('localhost', 9999))

s.listen(5)

while True:
    c, addr = s.accept()
    print("Connected With ", addr)
    print(c.recv(1024).decode())
    print(c.recv(1024).decode())
    age=int(c.recv(1024).decode())
    Year=2020-age
    Year=str(Year)
    c.send(bytes(Year,'utf-8'))

    c.close()
