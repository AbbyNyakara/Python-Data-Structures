"""
Implement the find_kth_from_end function, which takes the LinkedList (ll) 
and an integer k as input, and returns the k-th node from the end of the
linked list WITHOUT USING LENGTH.
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
        if self.head is None:  # empty
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

    def find_kth_from_end(self, k):
        '''Works for finding the Kth Node form the end:'''
        slow = self.head
        fast = self.head  # the fast node starts at the head

        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
          # The fast node is K places ahead

        # The fast and slow will move only 1 node at a time:
        # By checking that fast.next is not none,  you stop the loop before the fast pointer actually reaches the end of the list
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow.value


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)


print(linked_list.find_kth_from_end(3))

# linked_list.print_list()
