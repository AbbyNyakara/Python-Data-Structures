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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """Adds a node to the end of a linkedList . O(1)"""
        new_node = Node(value)
        if self.length == 0:  # Empty Linkedlist:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Find the tail , then the next should point to new node
            self.tail = new_node  # The new node becomes the tail
        self.length += 1

    def pop_last(self):
        """O(N)"""
        temp = self.head
        pre = self.head

        if self.length == 0:  # if the linkedlist is empty
            return None
        else:
            while temp.next:  # is not None
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1

            if self.length == 0:  # Say in the case where we had only 1 node:
                self.head = None
                self.tail = None

    def prepend(self, value):
        """Add a node at the beginning of a linkedList. O(1)"""
        new_node = Node(value)
        if self.length == 0:  # empty
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        self.length += 1

    def pop_first(self):
        """Remove the node at the beginning of a linkedlist"""
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None  # detach
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None

        return temp

    def get(self, index):
        """Fetch a Node at a certain index"""

    # def insert(self, value, index):
    #     """This will insert a new node at a certain index and add the length"""
    #     if index < 0 or index > self.length:
    #         return False

    #     if index == 0:  # If im inserting at the beginning
    #         self.length += 1
    #         return self.prepend(value)

    #     if index == self.length:
    #         self.length += 1
    #         return self.append(value)
    #     # Create the new Node
    #     new_node = Node(value)


linked_list = LinkedList(1)
linked_list.insert(4, 0)
linked_list.insert(6, 2)

linked_list.print_list()
