print("M O R E  E P I C  B A T T L E")

print("Select your move (R, P or S)")

player1name = input("What is Player 1 name? ")

player2name = input("What is Player 2 name? ")
player1score = 0

player2score = 0
RoundNumber = 1

while True:
    print(player1name, "'s score is", player1score, "and", player2name, "'s score is", player2score)

    

    print("Round,", RoundNumber)

    player1move = input(player1name + " what is your move? ")

    player2move = input(player2name + " what is your move? ")

    RoundNumber += 1

    if (player1move == "R" or player1move == "r") and (player2move == "S" or player2move == "s"):
        print(player1name, "smashes", player2name)
        player1score += 1
    elif (player1move == "R" or player1move == "r") and (player2move == "P" or player2move == "p"):
        print(player2name, "swallows", player1name)
        player2score += 1
    elif (player1move == "R" or player1move == "r") and (player2move == "R" or player2move == "r"):
        print("It is a tie!")
    elif (player1move == "P" or player1move == "p") and (player2move == "P" or player2move == "p"):
        print("it is a tie!")
    elif (player1move == "P" or player1move == "p") and (player2move == "S" or player2move == "s"):
        print(player2name, "cuts", player1name)
        player2score += 1
    elif (player1move == "P" or player1move == "p") and (player2move == "R" or player2move == "r"):
        print(player1name, "wraps", player2name)
        player1score += 1
    elif (player1move == "S" or player1move == "s") and (player2move == "R" or player2move == "r"):
        print(player2name, "smashes", player1name)
        player2score += 1
    elif (player1move == "S" or player1move == "s") and (player2move == "P" or player2move == "p"):
        print(player1name, "cuts", player2name)
        player1score += 1
    elif (player1move == "S" or player1move == "s") and (player2move == "S" or player2move == "s"):
        print("It is a tie!")
    else:
        print("It seems like you have entered an invalid entry, please enter either R, P or S!")
    
    if player1score == 3:
        print(player1name, "wins!")
        break
    elif player2score == 3:
        print(player2name, "wins!")
        break
    else:
        continue        
exit()


