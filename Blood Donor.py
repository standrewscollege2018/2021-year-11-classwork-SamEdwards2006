#This sets the weight and age limits
AGE_LIMIT = 18
WEIGHT_LIMIT = 50
#Takes the users age and weight
age = int(input("How old are you"))
weight = float(input("How much do you weigh in kilograms"))
#Decides whether or not the user is eligible
if age >= AGE_LIMIT and weight >= WEIGHT_LIMIT:
    print("You are eligible to donate blood")
else:
    print("You are not eligible to donate blood")x`