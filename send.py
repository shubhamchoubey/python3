#!/usr/bin/python3

import socket
import _thread

send_ip="127.0.0.1"
send_port=9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((send_ip,send_port))



def send():
	while True:
		msg=input().encode(encoding='utf-8', errors='strict')

		s.sendto(msg,("127.0.0.1",8888))
	

def recv():
	while True:

		recv_content=s.recvfrom(1000)

		string=recv_content[0].decode(encoding='utf-8', errors='strict')

		print(string)


_thread.start_new_thread(recv,())
_thread.start_new_thread(send,())
		
while True:
	pass	
		

