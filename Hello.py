#takes input from the user
stop = int(input("How many names do you wish to say: "))
#uses user input to print custom numbers
for num in range(1, stop + 1, 1):
    name = input("What is your name: ")
    print("Hello", name)
    stop = stop - 1
    print(stop, "Names to go")
print("Goodbye")