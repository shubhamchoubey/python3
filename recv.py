#!/usr/bin/python3

import socket
import time
import collections as cl 
rec_ip="127.0.0.1"
rec_port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((rec_ip,rec_port))
count=0
while True:
		
	recv_content=s.recvfrom(1000)	
	
	string=recv_content[0].decode(encoding='utf-8', errors='strict').split()
	count=cl.Counter(string)
	elements=sorted(count)
	for i in elements:
		print(i,count[i])

#	print(count)
#	count=count+str
#	time.sleep
		
	
