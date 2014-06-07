#Math module

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
