'''
Now make a new function cumulative sum that modiﬁes sum all so that instead of returning the sum of all the 
elements, it returns the cumulative sum; that is a new list where the i
th 
element is the sum of the ﬁrst i+1 elements 
from the original list. For example, the cumulative sum of [4, 3, 6] is [4, 7, 13]. 
'''

#Returns the sum of all numbers in a list
#Cumulative summing:

def cumSum(someList):
    answer = someList
    index = 0
    currentsum = 0
    for element in someList:
        currentsum += element
        answer[index] = currentsum
        index += 1
    return answer

a = [0, 1, 2, 3, 4, 5]

print cumSum(a)

b = [10000, 1000, 100, 10, 1]

print cumSum(b)
