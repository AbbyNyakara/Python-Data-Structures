"""
Write a method called swap_pairs inside the LinkedList class.
This method should swap every two adjacent nodes in the linked list by adjusting the pointers,
 not the node values.
You must modify the list in-place and update the head accordingly.
If the list has an odd number of nodes, the final node remains in its original position.
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

    def swap_pairs(self):
        # Because I will need to re-link the head: use dummy Node
        dummy = Node(0)
        dummy.next = self.head

        # Pointer to dummy
        temp = dummy

        first = temp.next

        while first is not None and first.next is not None:
            second = first.next
            # Switch them around
            first.next = second.next
            temp.next = second
            second.next = first
            # Now move to the next Pair:
            temp = first
            first = temp.next

        # Reset the head
        self.head = dummy.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.swap_pairs()

linked_list.print_list()
