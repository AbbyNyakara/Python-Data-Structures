class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.value = value
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        '''Appends a node to end of a ll'''
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        return new_node

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.next

    def partition_list(self, x: int):
        '''
        partitions the list such that all nodes with values 
        less than x come before nodes with values greater than or equal to x.
        '''

        if self.head is None:  # empty
            return None

        # The dummy nodes
        dummy1 = Node(0)
        dummy2 = Node(0)

        # Create the pointers
        less = dummy1
        greater = dummy2

        current = self.head

        while current is not None:
            if current.value < x:
                less.next = current
                # Then move it along:
                less = current
            else:
                greater.next = current
                greater = current

            current = current.next

        # Point the last Node of the
        # skips the 0th node
        # Less here is just the last node of the less than x nodes
        # Join the 2 lists
        less.next = dummy2.next

        self.head = dummy1.next
        self.tail = greater.next
        # or greater.next = None


linked_list = LinkedList(1)

linked_list.append(2)
linked_list.print_list()
