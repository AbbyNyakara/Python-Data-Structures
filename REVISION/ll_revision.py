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

    def append(self, value):
        """
        o(1)
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop(self):
        """
        Remove an element from teh end of a list and return the node
        - Empty
        - 1 Node
        - Multiple Nodes
        The time complexity is O(n)
        """
        if self.length == 0:
            return None

        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1

            return temp.value
        else:
            prev = None
            current = self.head

            while current != self.tail:
                prev = current
                current = current.next

            self.tail = prev
            prev.next = None

            return current.value


ll = LinkedList(1)
ll.append(21)
ll.append(7)

ll.print_list()
print("After popping")
ll.pop()
ll.print_list()
print("After popping")
ll.pop()
ll.print_list()
print("After popping")
ll.pop()
ll.print_list()
