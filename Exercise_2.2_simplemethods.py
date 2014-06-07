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


