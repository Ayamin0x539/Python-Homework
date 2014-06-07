#Exercise 1.7 - Rock, Paper, Scissors

#constants to print
p1win = "Player 1 wins."
p2win = "Player 2 wins."

while 1:
        
    p1 = raw_input("Player 1 chooses... ")
    p2 = raw_input("Player 2 chooses... ")

    if (p1 == p2):
        print "Tie."
    elif (p1 == "rock"):
        if (p2 == "scissors"):
            print p1win
        elif (p2 == "paper"):
            print p2win
    elif (p1 == "scissors"):
        if (p2 == "paper"):
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
