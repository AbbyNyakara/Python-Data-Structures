"""
Check to see if your linked list has a loop: That is if you were to traverse
 through the list , say the next attribute at the tail points to the head again
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        """Adds a node to the end of a linked list"""
        new_node = Node(value)
        if self.head is None:  # empty ll
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node

        return new_node

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def has_loop(self):
        """
        - 2 pointers : slow and fast
        - slow (1 step)
        - fast (2 steps)
        - is there's a loop, theyll meet at some point - return True
        - if fast reaches the end or encounters a none value, then no loop : return False
        """
        if self.head is None:
            return False
        if self.head == self.tail:
            return False

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next  # 2 steps

            if slow == fast:  # the same node
                return True
        return False




