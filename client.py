import sys
import socket
import json

alamatServer = "127.0.0.1"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((alamatServer, 2120))
pesan = "{\"id\": 42, \"method\": \"echo\", \"params\": {\"message\": \"Hello\"}}"
while pesan != "bye":
	s.send(pesan.encode())
	data = s.recv(1024).decode()
	print("Server : ", str(data))
	pesan = input(">")
s.close()