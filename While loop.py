keep_asking = True

#start asking their name
while keep_asking == True:
    name = input("Enter your name: ")
    if name == "Sam":
        keep_asking = False
    elif name == "sam":
        keep_asking = False
    else:
        print("Wrong name")
#loop is finished, so greet person
print("Hi Sam")