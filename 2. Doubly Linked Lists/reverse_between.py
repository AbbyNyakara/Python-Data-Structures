"""
DLL: Reverse Between ( ** Interview Question)
Write a method reverse_between that reverses a portion of a doubly linked list in place.
You are given a start index and an end index (inclusive range). Reverse only the nodes
between those indices.

Indexing is zero-based.
The list is made of nodes with both next and prev pointers.
Make sure the list remains fully connected after the reversal in both directions.
If the list has fewer than two nodes or the start and end indices are the same, 
leave the list unchanged.

Examples

Input:  1 <-> 2 <-> 3 <-> 4 <-> 5,  start_index = 1, end_index = 3  
Output: 1 <-> 4 <-> 3 <-> 2 <-> 5
 
Input:  10 <-> 20 <-> 30 <-> 40,  start_index = 0, end_index = 2  
Output: 30 <-> 20 <-> 10 <-> 40
 
Input:  1,  start_index = 0, end_index = 0  
Output: 1
"""


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

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def append(self, value):
        # Empty
        # Have some nodes
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    def reverse_between(self, start_index, end_index):

        if self.length < 2 or start_index == end_index:
            return
    
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy #add this for dll

        before = dummy 

        for _ in range(start_index):
            before = before.next # This is the node before the starting index:

        current = before.next

        for _ in range(end_index - start_index):
            temp = current.next
            # Detach temp from the list: 
            current.next = temp.next

            if temp.next:
                temp.next.prev = current

            # Move temp to the front of the sublist
            temp.next = before.next
            before.next.prev = temp
            before.next = temp
            temp.prev = before
            
        self.head = dummy.next
        # detach dummy node
        self.head.prev = None

new_dll = DoublyLinkedList(1)
new_dll.append(2)
new_dll.append(3)
new_dll.append(4)
new_dll.append(5)
new_dll.reverse_between(1,3)
new_dll.print_list()