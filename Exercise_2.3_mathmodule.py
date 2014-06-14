#Math module
'''
1. Many computations can be expressed concisely using the “multadd” operation, which takes three operands and 
computes a ∗ b + c. Write a function multadd that takes three parameters, a, b and c. Test your function well before moving on. 
2. Underneath your function deﬁnition, compute the following values using multadd and print out the result: 
... (omitted, characters unsupported)

If everything is working correctly, your output should look like: 
sin(pi/4) + cos(pi/4)/2 is:

1.06066017178

ceiling(276/19) + 2 log_7(12) is:

17.5539788165

3 3. Write a new function called yikes that has one argument and uses the multadd function to calculate the
following:
... (omitted, characters unsupported)

There are two diﬀerent ways to raise e to a power- check out the math module documentation. Be sure to

return the result! Try x=5 as a test; your answer should look like:

yikes(5) is 1.0303150673.
'''
import math

def degToRadian(degree):
    return (degree * math.pi / 180)

#math.degrees(x) converts angle x from radians to degrees
#math.radians(x) converts angle x from degrees to radians


def multiadd(a, b, c):
    return a*b + c

angle_test = multiadd(math.cos(math.pi/4), 0.5, math.sin(math.pi/4))
print "sin(pi/4) + cos(pi/4)/2 is: " + str(angle_test)

ceiling_test = math.ceil(276/19.0) + 2 * math.log(12, 7)
print "ceiling(276/19) + 2log_7(12) is: " + str(ceiling_test)



def yikes(x):
    eToNegX = math.exp(-x)
    sqrtTerm = math.sqrt(1 - eToNegX)
    return multiadd(x, eToNegX, sqrtTerm)

print "yikes(5) is " + str(yikes(5))
