counter = 0
while True:
    print("What a wonderful day this is!")
    agree = input("Do you agree? ")
    if agree == "no":
        break
print("That's too bad, I thought it was!")
name = input("Anyway, what is your name? ")

age = input("Oh hello there " + name + " how old are you? ")

if age >= "18":
    print("Okay you are an adult", name)
else:
    print("Oh you are too young to be on here", name, age, "is far too young!")