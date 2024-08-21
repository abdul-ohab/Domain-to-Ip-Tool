
import socket
domain_name = input("Enter your domain: ")

ip = socket.gethostbyname(domain_name)
print(ip)