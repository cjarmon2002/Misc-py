import random
from sys import exit

guesses_made = 0

name = raw_input("What is your name?\n> ")

number = random.randint(1, 100)

print "%s I'm thinking of a number between 1 and 100." % name

while guesses_made < 10:
	guess = int(raw_input("Take a guess: "))

	guesses_made += 1

	if guess < number:
		print "Too low."
	elif guess > number:
		print "Too high."
	elif guess == number:
		print "Good job %s, you guessed the number in %d tries." % (name, guesses_made)
		exit(0)

print "Sorry, the number was %d. Better luck next time." % number