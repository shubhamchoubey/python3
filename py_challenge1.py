#!/usr/bin/env python3

import webbrowser
import time
import os
print('''
Press 1 : {enter anything : }
Press 2 : {image} 
Press 3 : {URL}
Press 4 : current date and time of system
Press 5 : open default web browser
Press 6 : ALL Network IP
Press 7 : enter domain and check Owner with email and contact if available
''')


user_choice=input('Enter choice : ')
if user_choice=='1':
     user_data=input('Enter Data : ').strip().split()
#print(user_data)
#os.system('firefox &')
     for i in user_data:
     	webbrowser.open_new_tab('https://www.google.com/search?q='+i)

if user_choice=='2':
     user_data=input('Enter Data : ').strip().split()
     for i in user_data:
     	webbrowser.open_new_tab('https://www.google.com/search?tbm=isch&q='+i)

if user_choice=='4':
#     user_data=input('Enter Data : ').strip().split()
     date=os.system('date') 
     print(date)   







