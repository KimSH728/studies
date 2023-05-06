import socket 

TCP_IP = "172.18.0.2"
TCP_PORT = 6674

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.connect((TCP_IP, TCP_PORT))

print('Connection Detected')

data = sock.recv(1024)
print("Recieved : ", data.decode())

message = input("Name : ")
sock.send(message.encode())

data = sock.recv(1024)
print("Recieved : ", data.decode())

message = input("ID : ")
sock.send(message.encode())

sock.close()
