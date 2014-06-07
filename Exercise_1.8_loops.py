#Exercise 1.8: For and while loops

#1
for i in range(1, 11):
    print "1/" + str(i) + " is " + str(1.0/i)
    
#2
def numberChecker(string):
    try:
        isNumber = int(string)
        return True
    except ValueError:
        print "Not an integer!"
        return False

u_input = raw_input("Input? ")
isNumber = False

while not isNumber:
    if(numberChecker(u_input)):
        isNumber = True
        i_input = int(u_input)
    else:
        u_input = raw_input("Please enter an integer. ")
        
while(i_input < 0):
    u_input = raw_input("Enter a positive number. ")
    #Need to check if input is a number again
    isNumber = False
    while not isNumber:
        if(numberChecker(u_input)):
            isNumber = True
            i_input = int(u_input)
        else:
            u_input = raw_input("Please enter an integer. ")
    i_input = int(u_input)
while(i_input >= 0):
    print i_input
    i_input -= 1

#3
base = raw_input("Raise... ")
exp = raw_input("to the power of... ")
isNumber = numberChecker(base) and numberChecker(exp)
while not isNumber:
    base = raw_input("Please enter a base that's a number. ")
    exp = raw_input("Please enter an exponent that's a number. ")
    isNumber = numberChecker(base) and numberChecker(exp)
i_base = int(base)
i_exp = int(exp)
answer = 1
for i in range(i_exp):
    answer *= i_base
if i_base == 0:
    answer = 0
if i_exp == 0:
    answer = 1
print base + " raised to the power of " + exp + " is " + str(answer)

#4
s_number = raw_input("Enter a number that's divisible by two. ")
isNumber = numberChecker(s_number)
while not isNumber:
    s_number = raw_input("That's not even a number. Try again. ")
    isNumber = numberChecker(s_number)
i_number = int(s_number)
while i_number % 2 != 0:
    s_number = raw_input("That's not divisible by two. Try again. ")
    isNumber = numberChecker(s_number)
    while not isNumber:
        s_number = raw_input("That's not even a number. Try again. ")
        isNumber = numberChecker(s_number)
    i_number = int(s_number)
print "Yes, " + s_number + " is divisble by 2."
