import sys
import os

name = sys.argv[1]
directory = os.path.dirname(os.path.realpath(__file__))

with open("/etc/hosts") as f:
	lines = f.readlines()
	for l in lines:
		if(l.find(name)<0):
			print(l, end="")
	f.close()