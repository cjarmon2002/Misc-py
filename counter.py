print "Enter a number to have python count for you, enter 0 to exit"

count = 'a'

while count != 0:
	count = int(raw_input("> "))
	i = 0
	numbers = []
	while i < (count + 1):
		#print "i = %d" % i
		if i != 0:
			numbers.append(i)

		i += 1
	if count != 0:
		for num in numbers:
			print num
