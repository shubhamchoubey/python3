#!/usr/bin/python3

import socket
import base64
import _thread

rec_ip="127.24.25.30"
rec_port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((rec_ip,rec_port))

def recv():
	while True:
		recv_content=s.recvfrom(1000)	
		decrypt=base64.b64decode(recv_content[0])	
		string=decrypt.decode(encoding='utf-8', errors='strict').split()
		string_cor=""
		for i in range(len(string)):
			string_cor=string_cor+" "+string[i]
			
		print(string_cor.lstrip())

#	time.sleep(1)
def send():
	while True:
		encrypt=base64.b64encode
		msg=encrypt(input().encode(encoding='utf-8', errors='strict'))
	
		s.sendto(msg,('127.24.25.1',9999))


	
_thread.start_new_thread(send,())
_thread.start_new_thread(recv,())

while True:
	pass	

	

	
	
	




	
