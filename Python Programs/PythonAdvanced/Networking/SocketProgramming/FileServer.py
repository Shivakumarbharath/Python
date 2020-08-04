import socket

host = 'localhost'

port = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # this will return a socket

sock.bind((host, port))  # to bind

print('Server listening on port {}'.format(port))
sock.listen(5)  # it can connect to 5 clients in que

# To make it continous use a while loo[

c, add = sock.accept()
filename = c.recv(1024)  # recieving a file name frome the client
try:

    f = open(filename, 'rb')  # opening the file
    content = f.read()
    c.send(content)  # sending the contents back to the file
    f.close()
except FileNotFoundError:
    c.send(b'File Not Found')
c.close()
