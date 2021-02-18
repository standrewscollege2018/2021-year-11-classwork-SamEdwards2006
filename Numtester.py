#sets variables and imports time package
keep_asking = True
import time

while keep_asking == True:
    #Keeps asking until the player enters a number
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        #once a number is entered, the code stops asking
        keepasking = False
        #prints the two numbers
        print("your two numbers were {} and {}".format(num1, num2))
        time.sleep(2)
        #tests which of the numbers is biggest 8u8uihj7bm nhgy6humknjhyhynkjb587injh76jbihu6ihuy77bjihu7uhyg5fhugyhugyuhygtnjbhgytyjnbhg6tf56n7uy6tu7yt6567in7jubhyt

        if num1 > num2:
            print("The largest number was {}".format(num1))
        elif num2 > num1:
            print("The largest number was {}".format(num2))
        else:
            print("Your two numbers were the same")
        time.sleep(2)
        #prints the sum of the numbers
        print("The sum of your numbers is", num1 + num2)
    except:
        print("Enter an integer")