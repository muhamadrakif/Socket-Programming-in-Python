import sys
import socket
import json

lokasi = socket.gethostbyname("127.0.0.1")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((lokasi, 2120))
s.listen(5)
print("Server sudah aktif")
client, alamat = s.accept()
print("Menerima koneksi dari : ", alamat)
while True:
	data = client.recv(1024).decode()
	if not data:
		break
	print("Messege :", str(data))
	try:
		data_dict = json.loads(data)
		if (not str(data_dict['id']) or str(data_dict['method']) != "echo"):
			data_s = "error"
		else:
			data_s = "{" + "\"id\": " + str(data_dict['id']) + ", \"result\": " + str(data_dict['params']) + "}"
	except Exception as e:
		data_s = "error"

	client.send(data_s.encode())