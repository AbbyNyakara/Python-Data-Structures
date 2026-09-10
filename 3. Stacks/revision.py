class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
    Can be implemented as a list or as a linked list 
    """

    def __init__(self, value):
        new_node = Node(value)
        self.height = 1
        self.top = new_node

    def print_stack(self):
        """
        Prints all the values in the stack
        """

        temp = self.top

        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)

        if self.top is None:  # Stack empty
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1

    def pop(self):
        """
        Removes the node from the stack and returns the popped Node
        """
        if self.height == 0:
            return None
        
        temp = self.top
        if self.height == 1:
            self.top = None
            
        else:
            self.top = temp.next
            temp.next = None 

        self.height -= 1
        return temp.value






my_stack = Stack(1)
my_stack.push(4)
my_stack.push(8)
my_stack.print_stack()
print("After poopping")
my_stack.pop()
my_stack.print_stack()
