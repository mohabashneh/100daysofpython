print("EPIC ROCK PAPAER SCISSORS BATTLE!")

print("""Select your move by typing
      R for Rock
      P for Paper
      S for Scissors""")

user1 = input("Player 1 what is your name? ")

user2 = input("Player 2 what is your name? ")

player1 = input(f"{user1}, what is your move? ")

player2 = input(f"{user2}, what is your move? ")

if (player1 == "R" or player1 == "r") and (player2 == "S" or player2 == "s"):
    print(user1, "smashes", user2)
elif (player1 == "R" or player1 == "r") and (player2 == "P" or player2 == "p"):
    print(user2, "swallows", user1)
elif (player1 == "R" or player1 == "r") and (player2 == "R" or player2 == "r"):
    print("It is a tie!")
elif (player1 == "P" or player1 == "p") and (player2 == "P" or player2 == "p"):
    print("it is a tie!")
elif (player1 == "P" or player1 == "p") and (player2 == "S" or player2 == "s"):
    print(user2, "cuts", user1)
elif (player1 == "P" or player1 == "p") and (player2 == "R" or player2 == "r"):
    print(user1, "wraps", user2)
elif (player1 == "S" or player1 == "s") and (player2 == "R" or player2 == "r"):
    print(user2, "smashes", user1)
elif (player1 == "S" or player1 == "s") and (player2 == "P" or player2 == "p"):
    print(user1, "cuts", user2)
elif (player1 == "S" or player1 == "s") and (player2 == "S" or player2 == "s"):
    print("It is a tie!")
else:
    print("It seems like you have entered an invalid entry, please enter either R, PP or S!")