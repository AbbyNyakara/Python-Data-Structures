'''
Procedure: You might repeatedly take the next node after the current node and move 
it to the front of the sublist being reversed.
'''


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
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

        return new_node

    def print_list(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next

    def reverse_between(self, start_index, end_index):
        '''Assume that the indexes are valid and not out of range'''
        dummy = Node(0)

        dummy.next = self.head
        prev = dummy

        # Poosition the previous Node right before the current:
        for _ in range(start_index):
            prev = prev.next

        current = prev.next

        for _ in range(end_index-start_index):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        self.head = dummy.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.reverse_between(1, 3)
linked_list.print_list()
