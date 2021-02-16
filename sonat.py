#Sonar and light calculator
LIGHTSPEED = 299792458
SOUNDSPEED = 343
print("This program calculates the time taken for light or sound to travel a certain distance")
print("All outputs are rounded to the nearest Minute or Second")
while True:
    wave = int(input("ENTER 1 FOR LIGHT. ENTER 0 FOR SOUND: "))
    distance = int(input("DISTANCE TRAVELLED: "))
    if wave >= 1:
        result = distance / LIGHTSPEED
        if result >= 60:
            print(result // 60, "MINUTES")
        else:
            print(result // 1, "SECONDS")
    elif wave <= 0:
        result = distance / SOUNDSPEED
        if result >= 60:
            print(result // 60, "MINUTES")
        else:
            print(result // 1, "SECONDS")
    else:
        print(INVALID)
