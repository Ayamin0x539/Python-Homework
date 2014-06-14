# -*- coding: utf-8 -*-
'''
List comprehensions follow naturally from set builder notation and lambda calculus. They are very cool and make

your life a lot easier.

1. Write a list comprehension that prints a list of the cubes of the numbers 1 through 10. 
2. Write a list comprehension that prints out the possible results of two coin ﬂips (one result would be ’ht’). 
(Hint - how many results should there be?) 
3. Write a function that takes in a string and uses a list comprehension to return all the vowels in the string. 

'''


#1
print [x**3 for x in range(1, 11)]

#2
print [x+y for x in ['h', 't'] for y in ['h', 't']]

#3
def vowels(chars):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [x for x in chars if x in vowels]

print vowels("vowels")
