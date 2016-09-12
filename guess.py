import random

guessesTaken = 0

print("Hello what's your name?")

myName = raw_input()

number = random.randint(1,20)
print('Well,' + myName + ', I am thinking of a number between 1 and 20')
print("You have ")

while guessesTaken < 6:
	print("Take a guess")
	guess = input()
	guess = int(guess)

	guessesTaken += 1

	if guess < number:
		print("Your guess is too low")
	if guess > number:
		print("Your guess is too high")
	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print('Good job,' + myName + '! You got it right!')

if guess != number:
	number = str(number)
	print('Nope. The number I was thinking of was, ' + number)


