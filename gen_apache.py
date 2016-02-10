import sys
import os

name = sys.argv[1]
directory = os.path.dirname(os.path.realpath(__file__))

with open(directory+"/apache.conf") as f:
	lines = f.readlines()
	for l in lines:
		print(l.replace("{{name}}", name), end="");
	f.close()