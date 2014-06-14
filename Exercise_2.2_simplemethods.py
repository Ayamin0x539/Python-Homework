'''
Write a method is divisible that takes two integers, m and n. The method returns True if m is divisible by 
n, and returns False otherwise. Test cases for this function are included for you; look at the conditions that 
they test and try to make sure your future test cases are comprehensive. 
2 
2. Imagine that Python doesn’t have	the != operator built in. Write a method not equal that takes two
parameters and gives the same result as the != operator. Obviously, you cannot use != within your function! 
Test if your code works by thinking of examples and making sure the output is the same for your new method 
as != gives you. 
'''


#is_divisible

def is_divisible(m, n):
    return (m%n == 0)


print is_divisible(4, 2)
print is_divisible(5, 2)
print is_divisible(6, 2)
print is_divisible(7, 3)
print is_divisible(10, 2)

# Expected T, F, T, F, T

#not_equal
print "--- not equal ---"

def not_equal(x, y):
    if (x == y):
        return False
    else:
        return True

print not_equal(1, 2)
print not_equal(5, 5)
print not_equal(1, 10)
print not_equal(-2, -2)
print not_equal(14, 2)

# Expected T, F, T, F, T


