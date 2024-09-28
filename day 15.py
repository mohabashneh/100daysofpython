

stop = ""
while stop != "yes":
    cow = "cow goes MOOOO"
    chicken = "chicken goes BAQEEEEQ"

    inquire = input("What animal sound do you want? ")
    if inquire == "cow":
        print(cow)
    elif inquire == "chicken":
        print(chicken)
    else:
        again = input("Sorry, that animal is not available right now, can you please specify the animal again between a cow and a chicken? ")
        if again == "cow":
            print(cow)
        elif again == "chicken":
            print(chicken)
        else:
            print("Sorry, that animal is not available right now")
    stop = input("Do you wish to stop and exit? ")