import socket

UDP_IP = "172.18.0.3"
UDP_PORT = 6675
server_addr = (UDP_IP, UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

while True:
    message = input("Type the message to send: ")
    sock.sendto(message.encode(), server_addr) 
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message:", data.decode(), " from ", addr)
