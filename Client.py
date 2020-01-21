import socket
host = '127.0.0.1'
port = 12345
         
mySocket = socket.socket()
mySocket.connect((host,port))
message = input("hello")
         
while True:
	mySocket.send(message.encode())
	data = mySocket.recv(1024).decode()
                 
mySocket.close()
