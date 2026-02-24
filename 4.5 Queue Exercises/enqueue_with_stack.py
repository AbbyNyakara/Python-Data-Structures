"""
You are given a class MyQueue that implements a queue using two stacks.
Your task is to implement the enqueue method that should add an element
 to the back of the queue.

To achieve this, you can use the two stacks stack1 and stack2.
Initially, all elements are stored in stack1 and stack2 is empty.

To add an element to the back of the queue, you need to first transfer all elements from stack1 to stack2 using a loop that pops each element from stack1 and pushes it onto stack2.

Once all elements have been transferred to stack2, push the new element onto stack1. Finally, transfer all elements from stack2 back to stack1 in the same way as before, so that the queue maintains its ordering.

Your implementation should satisfy the following constraints:

The method signature should be def enqueue(self, value).

The method should add the element value to the back of the queue.
"""

# The whole concept of this is the First in first out. you have to create it such that when popping, 
# the first element in will be the first one out and so on

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return len(self.stack1) == 0


    def enqueue(self, value):
        if self.is_empty(): # if its empty 
            self.stack1.append(value)
        else: 
            while not self.is_empty():
                self.stack2.append(self.stack1.pop()) #remove the top element from stack 1 and add it to stack2
            self.stack1.append(value)
            
            while len(self.stack2) != 0:
                self.stack1.append(self.stack2.pop())

        return self.stack1
    

"""
# COURSE SOLUTION

def enqueue(self, value):
    while len(self.stack1) > 0:
        self.stack2.append(self.stack1.pop())
    self.stack1.append(value)
    while len(self.stack2) > 0:
        self.stack1.append(self.stack2.pop())
"""

            

        

