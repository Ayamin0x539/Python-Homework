'''
1. Write a method rand divis 3 that takes no parameters, generates and prints a random number, and ﬁnally 
returns True if the randomly generated number is divisible by 3, and False otherwise. For this method we’ll 
use a new module, the random module. At the top of your code, underneath import math, add the line 
import random. We’ll use this module to generate a random integer using the function randint, which works 
as follows: 
random.randint(lo, hi) 
where lo and hi are integers that tell the code the range in which to generate a random integer (this range 
is inclusive). 0 to 100 is probably a decent range. 
2. Write a method roll dice that takes in 2 parameters -the number of sides of the die, and the number of dice 
to roll - and generates random roll values for each die rolled.
'''

import random

#will use random.randint(lo, hi); returns a number from lo to hi inclusive

print "Random divisible by 3."

def rand_divis_3():
    rng = random.randint(0, 100)
    print "The random number generated is " + str(rng)
    print "Is it divisible by 3?: " + str(rng%3 == 0)

for i in range(0, 10):
    rand_divis_3()

print
print
print "Roll dice."

def roll_dice(sides, numDice):
    for die in range(numDice):
        rng = random.randint(1, sides)
        print "Die #" + str(die + 1) + " rolled a " + str(rng) + "."


roll_dice(6, 10)
