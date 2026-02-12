'''
Docstring for 10. Practice Questions.2.Palindrone

Write a method to determine whether a given doubly linked list reads the same forwards and backwards.

For example, if the list contains the values [1, 2, 3, 2, 1], then the method should return True, since the list is a palindrome.

If the list contains the values [1, 2, 3, 4, 5], then the method should return False, since the list is not a palindrome.

Method name:
is_palindrome

'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def print_list(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next

    def is_palindrome(self): # 2n
        forward = self.head
        backward = self.tail

        forward_values = []
        backward_values = []

        while forward:
            forward_values.append(forward.value)
            forward = forward.next

        while backward:
            backward_values.append(backward.value)
            backward = backward.prev

        
        if forward_values == backward_values:
            return True
        return False

    def palindrome_optimized(self): # n 
        if self.length == 1:  # for 1 node
            return True

        forward_node = self.head
        backward_node = self.tail

        for _ in range(self.length//2):
            if forward_node.value != backward_node.value:
                return False
            forward_node = forward_node.next
            backward_node = backward_node.prev
        return True





dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(2)
dll.append(1)
# dll.print_list()
print(dll.is_palindrome())




