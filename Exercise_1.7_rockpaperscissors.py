#Exercise 1.7 - Rock, Paper, Scissors
'''
In this exercise, you are going to practice using conditionals (if, elif, else). You will write a small program that will
determine the result of a rock, paper, scissors game, given Player 1 and Player 2’s choices. Your program will print 
out the result.
'''

#constants to print
p1win = "Player 1 wins."
p2win = "Player 2 wins."

while 1:
    print "Let's play rock, paper, scissors."
    p1 = raw_input("Player 1 chooses... ")
    p2 = raw_input("Player 2 chooses... ")

    if (p1 == p2 and (p1 == "rock" or p1 == "paper" or p1 == "scissors")):
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
    print
