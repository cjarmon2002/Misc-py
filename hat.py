import random

print """
Welcome to the electronic hat.
Enter the items you want to put in the hat.
The hat will automatically draw one item at random.
Enter 'done' after you have listed all of your items.
"""

items = "start"
hat = []

while items != "done":
	items = raw_input("> ")
	hat.append(items)
	print "The hat currently contains:", hat

hat.pop()

print "Removining 'done'."
print "The hat will pull from:"
print hat


random.shuffle(hat)


print "\nYour result is:\n"
print hat[0],"\n"