#Quadratic formula
'''
Write a function roots that computes the roots of a quadratic equation. Check for complex roots and print an 
error message saying that the roots are complex. 
'''
#in the form of ax^2 + bx + c = 0

def findRoots(a, b, c):
    discrim = b**2 - 4 * a * c #compute the discriminant
    if (discrim < 0):
        print "This quadratic equation has no real roots."
    else:
        root1 = (discrim**0.5 - b)/(2*a)
        root2 = (-(discrim**0.5) - b)/(2*a)
        print "The roots of the equation " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 are " + str(root1) + " and " + str(root2)

findRoots(1, 7, 12)
#(x+3)(x+4) = 0
findRoots(1, 3, -4)
#(x-1)(x+4) = 0
