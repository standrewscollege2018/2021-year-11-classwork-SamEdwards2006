#sets the arrest warrants
warrants = ["John Smith", "Helga Norman", "Zach Conroy"]
fine_total = 0
ask_count = 0
keep_asking = True
fine = 0
while keep_asking == True:
    #takes the name
    name = str(input("NAME: "))
   #if the name is in the warrants list, it will print this
    if name in warrants:
        print("ALERT: THERE IS AN ARREST WARRANT FOR", name)
   #if keep_asking == True:
        speedlimit = int(input("ENTER THE SPEED LIMIT: "))
        speed = int(input("ENTER THE SPEED OF THE VEHICLE: "))
        excess = speed - speedlimit
        if speed > speedlimit:
            if excess <= 10:
                fine = 30
            elif excess >= 10 and excess <= 19:
                fine = 80
            elif excess >= 20 and excess <= 29:
                fine = 130
            elif excess >= 30:
                fine = 180
            else:
                print("ERROR")
        else:
            print("")
        print("FINE: ${}".format(fine))
        fine_total = fine + fine_total
        ask_count = ask_count + 1
    #if the name inputed is "end", it stops the loop
    elif name == "end":
        keep_asking = False
    #if there is no warrant then it will ask for speed and speed limit
    else:
        print("THERE IS NO WARRANT FOR", name)
   #if keep_asking == True:
        speedlimit = int(input("ENTER THE SPEED LIMIT: "))
        speed = int(input("ENTER THE SPEED OF THE VEHICLE: "))
        excess = speed - speedlimit
        if speed > speedlimit:
            if excess <= 10:
                fine = 30
            elif excess >= 10 and excess <= 19:
                fine = 80
            elif excess >= 20 and excess <= 29:
                fine = 130
            elif excess >= 30:
                fine = 180
            else:
                print("ERROR")
        else:
            print("")
        print("")
        print("FINE: ${}".format(fine))
        fine_total = fine + fine_total
        ask_count = ask_count + 1
print("TOTAL NUMBER OF FINES:", ask_count)
print("TOTAL FINED: ${}".format(fine_total))