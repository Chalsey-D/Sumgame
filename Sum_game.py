#Sum game!!
#try to get the sum of 5 numbers

import random

def SumGame():
	numbers = random.sample(range(1, 11), 5)
	#numbers 1-10

	total = sum(numbers)
	print(numbers)
	
	while True:
		try:
			answer = int((input("What is the sum? ")))
		except ValueError:
			print("You must put in a number.")
			#Put in the wrong type of value such as a letter or non interger
			continue
		else:
			#A whole number was used
			break

	if answer == total:
		print("Correct! the sum is " + str(total) + ".")
		#if they got the answer right
	else:
		print("Incorrect! the sum is " + str(total) + ".")
		print("Your answer was " + str(answer) + ".")
		#if they got the answe wrong

SumGame()

again = input("Do you want to do another operation? (Y/N): ").upper()

while again == 'Y':
    if again == 'Y':
        SumGame()
        again = input("Do you want to do another operation? (Y/N): ").upper()

    else:
        pass

print("Have a good day!")