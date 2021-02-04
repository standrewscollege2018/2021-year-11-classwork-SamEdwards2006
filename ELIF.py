# Creates constants for the scores
A = 90
B = 70
C = 50
UPPER_LIMIT = 100
on = 1

while (on > 0):
    # takes the users score
    score = int(input("What was your score?"))
    # works out the grade based on predetermined constants
    # and decides if the score is too high
    if score > UPPER_LIMIT:
        print("That score is too high. the limit is {}.".format(UPPER_LIMIT))
    elif score >= A:
        print("You got an A")
    elif score >= B:
        print("You got a B")
    elif score >= C:
        print("You got a C")
    else:
        print("You failed")