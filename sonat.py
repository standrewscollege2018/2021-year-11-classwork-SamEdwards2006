#Sonar and light calculator
import time
LIGHTSPEED = 299792458
SOUNDSPEED = 343
KEEPASKING = True
LOOP = True
print("This program calculates the time taken for light or sound to travel a certain distance")
print("All outputs are rounded to the nearest Minute or Second")
while KEEPASKING == True:
    try:
        wave = int(input("ENTER 1 FOR LIGHT. ENTER 0 FOR SOUND: "))
        if wave == 1:
            distance = int(input("DISTANCE TRAVELLED: "))
            result = distance / LIGHTSPEED
            if result >= 60:
                print(result // 60, "MINUTES")
            else:
                print(result // 1, "SECONDS")
        elif wave == 0:
            distance = int(input("DISTANCE TRAVELLED: "))
            result = distance / SOUNDSPEED
            if result >= 60:
                print(result // 60, "MINUTES")
            else:
                print(result // 1, "SECONDS")
        elif wave == 69:
            print("WOW, you must be a comedian or something")
            time.sleep(1)
            print("No really, I'm cracking up lauging")
            time.sleep(1)
            print("I really love originality when it comes to humor")
            time.sleep(1)
            print("Go away")
            KEEPASKING == False
        else:
            print("INVALID")
    except:
        print("ENTER AN INTEGER")
print("Shutting down")