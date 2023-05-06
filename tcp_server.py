import socket 

TCP_IP = "0.0.0.0"
TCP_PORT = 6674

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)
print("Wait for connection")

consock, addr = sock.accept()
print('Connection from', str(addr))
consock.send("What is your name?".encode())

data = consock.recv(1024)
print("My name is ",data.decode())

consock.send("How about your ID?".encode())

data = consock.recv(1024)
print("MY ID is ",data.decode())

sock.close()
