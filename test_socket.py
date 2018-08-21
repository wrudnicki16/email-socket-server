import socket
import sys
import _thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# make a request to pythonprogramming.net by connecting to the server

host = 'pythonprogramming.net'
port = 80
server_ip = socket.gethostbyname(host)
print(server_ip)

request = "GET / HTTP/1.1\nHost: " + host + "\n\n"
s.connect((server_ip, port))
s.send(request.encode())
result = s.recv(4096)

print(result)