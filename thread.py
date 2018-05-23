#!/usr/bin/env python3

import _thread
import time 

def ok():
	while True:
		print("i am shubham")
		time.sleep(1)

def hello():
	while True:
		print('hi')
		time.sleep(2)
_thread.start_new_thread(ok,())
_thread.start_new_thread(hello,())

while True:
	pass
