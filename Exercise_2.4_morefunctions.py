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
