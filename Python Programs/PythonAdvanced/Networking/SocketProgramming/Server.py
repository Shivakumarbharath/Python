import socket

host = 'localhost'

port = 4000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # this will return a socket

sock.bind((host, port))  # to bind

print('Server listening on port {}'.format(port))
sock.listen(5)  # it can connect to 5 clients in que

# To make it continous use a while loo[
while True:
    c, add = sock.accept()
    '''
accepts method returns two things
1-it returns connections-c
2.it returns the address-add

so accept actually accepts the connections ,it establises a connection to client when the client requests a connection
it returns an object c and also the address of the client add
    '''

    print("Connection Established with {} ".format(str(add)))

    c.send(b"Hello ! \n How Are You")
    '''
# you have to encode this into binary by appeending b
Or can do using .encode

    '''

    c.send("Bye Client {} ".format(add).encode())

    c.close()
