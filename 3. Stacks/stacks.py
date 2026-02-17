class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, val):
        new_node = Node(value=val)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top

        while temp is not None:
            print(temp.value)
            temp = temp.next


    def push(self, value):
        """Adds a node to the top of the stack"""
        new_node = Node(value=value)

        # 2 Edge cases: empty stack, and stack with nodes
        if self.height == 0:
            self.top = new_node

        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1

    def pop(self):
        """removes a node from the top of the stack"""
        if self.height == 0:
            return None # Nothing to pop
        
        else: 
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1

        return temp


stack = Stack(4)
stack.push(2)
stack.push(7)
stack.push(12)
stack.print_stack()
print("After popping")
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.print_stack()

