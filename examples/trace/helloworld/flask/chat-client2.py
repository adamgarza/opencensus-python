import socket

s = socket.socket()
host = '' #socket.gethostname()
port = 8888
s.connect((host, port))
z = ''

while True:
    z = raw_input("Message: ")
    s.send(z)
    print ("Waiting for reply")
    print (s.recv(1024))