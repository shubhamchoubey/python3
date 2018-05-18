#!/usr/bin/python3

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	msg=input('enter : ').encode(encoding='utf-8', errors='strict')
	s.sendto(msg,("127.0.0.1",8888))

