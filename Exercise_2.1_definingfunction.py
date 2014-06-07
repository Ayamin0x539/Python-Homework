#Defining a function: Rock paper scissors

def rps(p1, p2):
    p1win = "Player 1 wins."
    p2win = "Player 2 wins."
    if (p1 == p2):
        print "Tie."
    elif (p1 == "rock"):
        if (p2 == "scissors"):
            print p1win
        elif (p2 == "paper"):
            print p2win
    elif (p1 == "scissors"):
        if(p2 == "paper"):
            print p1win
        elif (p2 == "rock"):
                print p2win
    elif (p1 == "paper"):
        if (p2 == "rock"):
            print p1win
        elif (p2 == "scissors"):
            print p2win
    else:
        print "Invalid input."

rps("rock", "paper")
rps("lol", "hi")
rps("paper", "paper")
rps("paper", "rock")
rps("scissors", "rock")
