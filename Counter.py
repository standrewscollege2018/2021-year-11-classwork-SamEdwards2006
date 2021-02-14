#takes input from the user
start = int(input("What number should I start at: "))
stop = int(input("What number should I stop at: "))
step = int(input("what should the step be: "))
#uses user input to print custom numbers
for num in range(start, stop + 1, step):
    print(num)