"""
Python Data Structures & Algorithms + LEETCODE Exercises
Stack: Parentheses Balanced ( ** Interview Question)
Check to see if a string of parentheses is balanced or not.

By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, 
so it is a balanced string. On the other hand, the string "(()))" has an 
imbalance, as the last two parentheses do not match, so it is not balanced. 
 Also, the string ")(" is not balanced because the close parenthesis needs to 
 follow the open parenthesis.

Your program should take a string of parentheses as input and return True 
if it is balanced, or False if it is not. In order to solve this problem, 
use a Stack data structure.

Function name:
is_balanced_parentheses

Remember: this is not a method within the Stack class, this is a separate function. 
 Indent all the way to the left.

This will use the Stack class we created in these coding exercises:
"""


class Stack:
    def __init__(self):
        self.stacked_list = []

    def print_stack(self):
        for i in range(len(self.stacked_list)-1, -1, -1):
            print(self.stacked_list[i])

    def push(self, value):
        return self.stacked_list.append(value)

    def pop(self):
        return self.stacked_list.pop()

    def is_empty(self):
        return len(self.stacked_list) == 0


def is_balanced_parentheses(string):
    stack = Stack()

    for i in string:
        if i == "(":
            stack.push(i)
        elif i==")":
            if stack.is_empty():
                return False
            stack.pop()

    return stack.is_empty()

print(is_balanced_parentheses("("))