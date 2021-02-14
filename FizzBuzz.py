#FIZZBUZZ
number = int(input("What number should we count to: "))
num1 = int(input("What is number 1: "))
num2 = int(input("What is number 2: "))
fizz = input("What should we say when the number is a multiple of num1")
buzz = input("What should we say when the number is a multiple of num2")
count_number = 1
for num in range(0, number + 1, 1):
    if ((count_number %num1 == 0) and (count_number %num2 == 0)):
        print(fizz+buzz)
    elif (count_number %num1 == 0):
        print(fizz)
    elif (count_number %num2 == 0):
        print(buzz)
    else:
        print(count_number)
    count_number = count_number + 1