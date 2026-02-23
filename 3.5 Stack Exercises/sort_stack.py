"""
The sort_stack function takes a single argument, a Stack object. 
 The function should sort the elements in the stack in ascending order 
 (the lowest value will be at the top of the stack) using only one additional stack. 

The function should use the pop, push, peek, and is_empty methods of the Stack object.

Note: This is a new function, not a method within the Stack class. 
So, your indent should be all the way to the LEFT.

This will use the Stack class we created in these coding exercises:

The function should perform the following tasks:

Create a new instance of the Stack class called sorted_stack.

While the input stack is not empty, perform the following:

Pop the top element from the input stack and store it in a variable temp.

While the sorted_stack is not empty and its top element is greater than temp,
 pop the top element from sorted_stack and push it back onto the input stack.

Push the temp variable onto the sorted_stack.

Once the input stack is empty, transfer the elements back from sorted_stack 
to the input stack. To do this, while sorted_stack is not empty, pop the top
element from sorted_stack and push it onto the input stack.

    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""


class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        # i is essentially the index:
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def push(self, value):
        return self.stack_list.append(value)

    def pop(self):
        return self.stack_list.pop()

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]


def sort_stack(old_stack):
    sorted_stack = Stack()

    while not old_stack.is_empty():
        temp = old_stack.pop()  # get the top element from the unsorted stack
        peek_value = sorted_stack.peek()  # gets the top element from the sorted stack

        while not sorted_stack.is_empty():  # while the sorted stack is not empty
            if temp > peek_value:
                sorted_stack.pop()
                old_stack.push(peek_value)
            else:
                sorted_stack.push(temp)

    return sorted_stack


