import socket
#use to find ip of your machine
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print(IPAddr)

