#sets the which year you want to test for
YEAR = 2021
#takes the users data
name = str(input("What is your name?: "))
age = int(input("What year were you born?: "))
# prints the statement
print(name, "will be", YEAR - age, "in 2021")