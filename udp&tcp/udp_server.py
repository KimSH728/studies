import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 6675

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvsfrom(1024) # buffer size is 1024 bytes
    print("received message:", data.decode(), " from ", addr)
    message = input("Type the message to send: ")
    sock.sendto(message.encode(), addr)
