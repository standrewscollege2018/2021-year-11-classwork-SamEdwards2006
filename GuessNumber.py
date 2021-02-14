#imports depository
import random
Solved = False
num = random.randint(-100, 100)
guess = 0
#counts the guesses and tests if the the number is too high or too low
while Solved == False:
    num_input = int(input("Guess a number: "))
    if num_input == num:
        Solved = True
    elif num_input <= -100:
        print("TOO LOW. GO WAY HIGHER!!")
        guess = guess + 1
    elif num_input >= 100:
        print("TOO HIGH. GO WAY LOWER!!")
        guess = guess + 1
    elif num_input >= num:
        print("Lower")
        guess = guess + 1
    elif num_input <= num:
        print("Higher")
        guess = guess + 1
print("Correct")
#prints the amount of tries it took the user
print("it took you", guess, "tries")