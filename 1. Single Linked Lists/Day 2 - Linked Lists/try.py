class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def prepend(self, value):
        """
        Add a node at the beginning 
        """


        # step 1- create a new node:
        new_node = Node(value)
        # step 2 - create a variable to hold the head
        temp = self.head
        # step 3 - assign the head to the new node:
        self.head = new_node
        # The next node becomes the temp
        self.head.next = temp
        self.length += 1

        