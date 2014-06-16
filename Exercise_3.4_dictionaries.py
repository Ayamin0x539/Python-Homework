# -*- coding: utf-8 -*-

'''
NAMES = [’Alice’, ’Bob’, ’Cathy’, ’Dan’, ’Ed’, ’Frank’, 
’Gary’, ’Helen’, ’Irene’, ’Jack’, ’Kelly’, ’Larry’] 
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

These lists match up, so Alice’s age is 20, Bob’s age is 21, and so on.
Write a function combine_lists that combines these lists into a dictionary.
(hint: what should the keys, and what should the values, of this dictionary be?)
Then, write a function people that takes in an age and returns the names of all the people who are that age. 

Test your program’s functions by running these lines (they are commented at the bottom of the code ﬁle; uncomment 
them to use them): 
print ’Dan’ in people(18) and ’Cathy’ in people(18) 
print ’Ed’ in people(19) and ’Helen’ in people(19) and\ 
’Irene’ in people(19) and ’Jack’ in people(19) and ’Larry’in people(19) 
print ’Alice’ in people(20) and ’Frank’ in people(20) and ’Gary’ in people(20) 
print people(21) == [’Bob’] 
print people(22) == [’Kelly’] 
print people(23) == []

'''

def combine_lists(list_a, list_b):
    combination = {}
    index = 0
    for element in list_a:
        combination[element] = list_b[index]
        index += 1
    return combination

NAMES = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank", "Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"]
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

dictionary = combine_lists(NAMES, AGES)

print dictionary

def people(age):
    answer = []
    keys = dictionary.keys() # a list of all the keys
    for element in keys:
        if dictionary[element] == age: #if the key's value is equal to the age, append the key to the list
            answer.append(element) #that we will return
    return answer
    
print "Dan" in people(18) and "Cathy" in people(18) 
print "Ed" in people(19) and "Helen" in people(19) and\
"Irene" in people(19) and "Jack" in people(19) and "Larry" in people(19) 
print "Alice" in people(20) and "Frank" in people(20) and "Gary" in people(20) 
print people(21) == ["Bob"] 
print people(22) == ["Kelly"] 
print people(23) == []
