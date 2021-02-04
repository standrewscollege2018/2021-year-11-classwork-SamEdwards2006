#sets the constants
AGE_LIMIT = 12
WEIGHT_LIMIT = 0
on = 1
#finds the users age
while(on > 0):
    age = int(input("How old are you: "))
    #tests if the age is more than 12,
    #if not, it will go to the else.
    if age >= AGE_LIMIT:
        print("Recommend two 500 mg paracetamol tablets")
    elif age >= 0:
        #takes the users weight, and if it is more than 0
        # it will multiply the weight by 10
        weight = float(input("How much do you weigh: "))
        if weight > WEIGHT_LIMIT:
            print("Your recommended dose is", weight * 10,"mg")
        else:
            print("invalid weight")
    else:
        print("invalid age")

