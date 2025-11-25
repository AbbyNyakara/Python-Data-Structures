"""
Find the middle node in a linkedlIst. You can only iterate through the list once. And also yoou are
not allowed to calcute the lenght of the list. 
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
        """Adds a node to a linkedlist """
        new_node = Node(value)
        if self.head is None:  # empty
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            # when temp.next becomes none, Ive gotten to the end of ll
            temp.next = new_node
            new_node.next = None
            self.tail = new_node
        return new_node

    def print_list(self):
        """Prints the linkedList"""
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def find_middle_node(self):
        """Find middle node, return the node"""
        if self.head is None:
            return None
        
        if self.head == self.tail:
            return self.head

        slow = self.head # The slow will only move 1 step
        fast = self.head

        while fast is not None and fast.next is not None:  # the fast is not at the tail
            slow = slow.next
            fast = fast.next.next

        return slow


linkedlist = LinkedList(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(5)
linkedlist.append(6)
linkedlist.append(7)

print(linkedlist.find_middle_node().value)



