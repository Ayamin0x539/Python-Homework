# -*- coding: utf-8 -*-
'''
This problem builds on your work in Exercise 3.6. Stacks are the opposite of queues - instead of being ‘ﬁrst-in­
ﬁrst-out’, they use a ‘last-in-ﬁrst-out’ (LIFO) strategy. Think of them like a pop-up stack of plates at a restaurant; 
the ﬁrst plate put in will be the last one pulled out and used. Again, check out Wikipedia for a more in-depth 
explanation. 
Make a new ﬁle stacks.py and implement a Stack class. It should be very similar to your Queue implementation; 
the three methods your class will need will be init , push, and pop. 
When you’re done, you should test your implementation. Your results should look like this:

>> stack = Stack()
>> stack.push(5)
>> stack.push(6)
>> stack.pop()
6
>> stack.push(7)
>> stack.pop()
7
>> stack.pop()
5
>> stack.pop()
The stack is empty
'''

class Stack():
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if (self.elements == []):
            print "The stack is empty."
            return
        top = self.elements[len(self.elements)-1]
        self.elements.remove(top)
        return top

stack = Stack()
stack.push(5)
stack.push(6)
print stack.pop()
stack.push(7)
print stack.pop()
print stack.pop()
print stack.pop()
