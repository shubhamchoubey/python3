#!/usr/bin/python3

import socket
import _thread
import base64

send_ip="127.24.25.1"
send_port=9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((send_ip,send_port))



def send():
	while True:
		encrypt=base64.b64encode
		msg=encrypt(input().encode(encoding='utf-8', errors='strict'))

		s.sendto(msg,("127.24.25.30",8888))
	

def recv():
	while True:

		recv_content=s.recvfrom(1000)
#		print(recv_content)
		decrypt=base64.b64decode(recv_content[0])
		
		string=decrypt.decode(encoding='utf-8', errors='strict')

		print(string)


_thread.start_new_thread(recv,())
_thread.start_new_thread(send,())
		
while True:
	pass	
		

