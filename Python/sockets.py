import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )
# encode() takes in the string and converts it into Bytes
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    # data here is in bytes
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    # here the data is decoded in Unicode format
    print (data.decode())
mysock.close()
