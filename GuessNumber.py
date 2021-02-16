#imports depository
import random
import time
y = 1
n = 0
Solved = False
keepplaying = "y"
guess = 1
highscore = random.randint(1000000,10000000)
#counts the guesses and tests if the the number is too high or too low
while keepplaying == "y":
    Solved = False
    num = random.randint(-100, 100)
    while Solved == False:
        num_input = int(input("Guess a number between -100 and 100: "))
        if num_input == num:
            Solved = True
        elif num_input <= -101:
            print("TOO LOW. GO WAY HIGHER!!")
            guess = guess + 1
        elif num_input >= 101:
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
    #if the guesses is less than the highscore then it changes the highscore
    if guess < highscore:
        highscore = guess
        print("Your new high score is", highscore)
    else:
        print("Your highscore is {}. keep playing to get a better score".format(highscore))
    #asks the player to play again
    keepplaying = str(input("Would you like to play again. (y/n): "))
print("Goodbye")#imports depository