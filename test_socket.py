import socket
import sys
import _thread
import requests

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# make a request to pythonprogramming.net by connecting to the server

# host = 'pythonprogramming.net'
# port = 80
# server_ip = socket.gethostbyname(host)
# print(server_ip)

# request = "GET / HTTP/1.1\nHost: " + host + "\n\n"
# s.connect((server_ip, port))
# s.send(request.encode())
# result = s.recv(4096)

# print(result)

# create socket
# s = socket.socket()
port = 5555
host = ''


# bind socket and listen for connections
try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

print('waiting for a connection...')

s.listen(5)

def threaded_client(conn):
    conn.send(str.encode('Welcome, type your info\n'))
    while True:
        data = conn.recv(2048)
        reply = handle_data(data)
        # reply = 'Server output: ' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))

    conn.close()

def handle_data(data):
    string = data.decode('utf-8')
    if string.startswith('http://') or string.startswith('https://'):
        print('hopefully this is ')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        req = requests.get(string, headers=headers)
        print(req.content)

        return 'Here is the src info for this url, that is if you can call get on it:\n\n' + req.content.decode('utf-8')
        

    return 'Server response: ' + string

# Establish a connection with the client (socket must be listening)
while True:
    conn, addr = s.accept()
    print('connected to: ' + addr[0] + ':' + str(addr[1]))

    _thread.start_new_thread(threaded_client, (conn, ))
