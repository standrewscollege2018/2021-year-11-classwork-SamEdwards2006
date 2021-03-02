keepasking = True
names = []
import time
import random
while(keepasking == True):
    var1 = str(input("Would you like to enter another name: "))
    if(var1 == "yes"):
        names.append(input("Enter a name: "))
    else:
        keepasking = False
print("There are", len(names), "entrys")
for i in range(len(names)):
    print(names[i])
chance = 100/len(names)
print("Each entry has a", chance, "percent chance of winning")
prize = str(input("What is the prize: "))
time.sleep(1)
print("AND THE WINNER IS")
time.sleep(1)
for num in range(0, 50, 1):
   # if (num % 2):
    #    print()
    #else:
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("                 DRUMROLL                  ")
    time.sleep(.1)
winner = random.randint(0, len(names))
print(names[winner-1])