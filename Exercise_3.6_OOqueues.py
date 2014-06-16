# -*- coding: utf-8 -*-
'''
In your Queue class, you will need three methods: 
•	 __init__ : to initialize your Queue (think: how will you store the queue’s elements? You’ll need to initialize 
an appropriate object attribute in this method) 
•	 insert: inserts one element in your Queue 
•	 remove: removes one element from your Queue and returns it. If the queue is empty, return a message that 
says it is empty. 
When you’re done, you should test your implementation. Your results should look like this: 
>> queue = Queue() 
>> queue.insert(5) 
>> queue.insert(6) 
>> queue.remove() 
5 
>> queue.insert(7) 
>> queue.remove() 
6 
>> queue.remove() 
7 
>> queue.remove() 
The queue is empty 
Be sure to handle that last case correctly - when popping from an empty Queue, print a message rather than 
throwing an error. 
'''

class Queue:
    def __init__(self):
        self.elements = []

    def insert(self, element):
        self.elements.append(element)

    def remove(self):
        if (self.elements == []):
            print "The queue is empty."
            return
        top = self.elements[0]
        self.elements = self.elements[1:]
        return top


queue = Queue()
queue.insert(5)
queue.insert(6)
print queue.remove()
queue.insert(7)
print queue.remove()
print queue.remove()
print queue.remove()
