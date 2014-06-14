# Represent a ball on a plane as a tuple of (x, y, r), r being the radius

#If (distance between two balls' centers) <= (sum of their radii)
# then (they are colliding)

def ball_collide(ball_1, ball_2):
    x1, y1, r1 = ball_1
    x2, y2, r2 = ball_2
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    radiisum = r1 + r2
    if (distance <= radiisum):
        return True
    return False


# Test Cases for Exercise 3.2
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True
