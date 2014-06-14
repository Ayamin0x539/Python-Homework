#The game of Nims/Stones
'''
In this game, two players sit in front of a pile of 100 stones.
They take turns, each removing between 1 and 5 stones
(assuming there are at least 5 stones left in the pile).
The person who removes the last stone(s) wins.
'''

def isNumber(string):
    try:
        number = int(string)
        return True
    except ValueError:
        print "That's not an integer."
        return False

def play_nims(pile, max_stones):
    stonesLeft = pile
    print "There are " + str(pile) + " stones in the pile."
    while(1):
        #Player 1
        validInput = False
        while(not validInput):
            s_remove = raw_input("Player 1, how many stones would you like to remove? ")
            validInput = isNumber(s_remove)
            if (validInput):
                i_remove = int(s_remove)
                if (i_remove < 1 or i_remove > max_stones):
                    validInput = False
                    print "Please enter an amount between 1 and " + str(max_stones) + "."
        if (i_remove >= stonesLeft):
            print "Player 1 wins!"
            break
        else:
            stonesLeft -= i_remove
            print "There are " + str(stonesLeft) + " stones left."

        #Player 2
        validInput = False
        while(not validInput):
            s_remove = raw_input("Player 2, how many stones would you like to remove? ")
            validInput = isNumber(s_remove)
            if (validInput):
                i_remove = int(s_remove)
                if (i_remove < 1 or i_remove > max_stones):
                    validInput = False
                    print "Please enter an amount between 1 and " + str(max_stones) + "."
        if (i_remove >= stonesLeft):
            print "Player 2 wins!"
            break
        else:
            stonesLeft -= i_remove
            print "There are " + str(stonesLeft) + " stones left."


play_again = True
while(play_again):
    isInt = False
    while(not isInt):
        start = raw_input("How many stones would you like to start with? ")
        isInt = isNumber(start)
        if (isInt):
            i_start = int(start)
    isInt = False
    while(not isInt):
        maxStones = raw_input("What is the max amount of stones that can be removed? ")
        isInt = isNumber(maxStones)
        if (isInt):
            i_maxStones = int(maxStones)
    print "Beginning Nims/Stones with " + start + " stones. You can remove up to " + maxStones + " stones at a time."
    play_nims(i_start, i_maxStones)
    yesno = ''
    while(not ((yesno == "yes") or (yesno == "no"))):
        yesno = raw_input("Would you like to play again? (yes/no) ")
        if (yesno == "yes"):
            play_again = True
        elif (yesno == "no"):
            play_again = False
            print "We'll stop playing then."
        else:
            print "Please enter either \"yes\" or \"no\"."






    
