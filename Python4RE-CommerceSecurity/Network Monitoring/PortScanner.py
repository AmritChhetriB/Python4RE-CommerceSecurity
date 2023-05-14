import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for port in range(80, 81):
	print(port)
	con = s.connect(("192.168.163.1", port))
	if con==None:
		print('Port', port,'is open')
	else:
		print('Port', port,'is close')
	s.close()
		

