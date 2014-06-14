#Defining a function: Rock paper scissors
'''
Recall how we deﬁne a function using def, and how we pass in parameters. In homework 2.py (download this 
from the website if you haven’t yet), transform your code from exercise 1.7 (the rock, paper, scissors game) into a 
function that takes parameters, instead of asking the user for input. Make sure to return your answer, rather than 
printing it. 
'''

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
