names = []
length = int(input("How many names do you want to add: "))
for num in range(0, length, 1):
    names.append(input("What is your name: "))
#for n in names:
#   print(n)

for i in range(len(names)):
    print(i+1, names[i])