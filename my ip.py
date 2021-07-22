import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"My ip address : {ip_address}")