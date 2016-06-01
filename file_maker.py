import os.path
from sys import exit

x = raw_input("Name your file. ")
if os.path.isfile(x+".txt") == True:
	print "That file exist"
	exit(0)
else:
	f = open(x+".txt", "w+")
	f.write("This is your new file\n")
	f.close()
	# f = open(x+".txt", "r+")
	# print f.read()
	# f.close()