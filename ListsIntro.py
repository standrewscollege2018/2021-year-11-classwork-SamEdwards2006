#this program demonstrates how lists work

#for lists, we use square brackets
keepasking = False
names = [""]

#to print a list use

print(names)

#to print an individual item of a list
#we use it's index position in the list

print(names[0])

#to add an item to a list we use append()
while keepasking == True:
    names.append(input("what is your name: "))
    print(names)

#lists are mutable (can be changed)
#to change the value of something, we just overwrite it


#to find the length of a list use
print(len(names))