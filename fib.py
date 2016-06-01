(a, b) = (1, 1)
fib = []
(c, d) = (1, 1)
fibb = []
end = int(raw_input("How high would you like the fibonacci sequence to go? > "))

while a <= end:
	fib.append(a)
	(a, b) = (b, a+b)


for num in fib:
	print num

#print fib
print "\n"

end2 = int(raw_input("Lets do it twice, how many steps of the sequence would you like? > "))


for i in range(0, end2):
	print c
	(c, d) = (d, c+d)