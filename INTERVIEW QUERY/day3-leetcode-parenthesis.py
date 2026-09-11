"""
iven a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

- Hint 1 : USE A STACK 
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def push(self, value):
        new_node = Node(value)

        # Case 1 - empty
        if self.length == 0:
            self.top = new_node
        else:
            self.top.next = new_node
            self.top = new_node

        self.length += 1

    def pop(self):
        """
        Removes the top node
        """
        if self.length == 0:
            return None

        temp = self.top
        self.top = self.top.next

        temp.next = None
        self.length -= 1
        return temp.value

    def print_queue(self):
        temp = self.top

        while temp:
            print(temp.value)
            temp=temp.next

    def peek_top(self):
        return self.top.value

    def is_empty(self):
        return self.length == 0 or self.top is None



