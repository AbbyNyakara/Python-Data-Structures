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
        Adds a node to the end of a linkedlist

        Case 1: Empty linkedList:
        Case 2: There's one or more nodes:
        """
        new_node = Node(value)
        if self.head is None:  # linkedlist is empty:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next

    def pop(self):
        """
        Removes the node at the end of a linkedlist and returns it

        case 1: Empty LinkedList
        case 2: Only one node
        case 3: 1 or more
        """

        if self.head is None:
            return None
        
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            return temp
        else:
            prev = None
            temp = self.head 

            while temp.next is not None:
                prev = temp
                temp = temp.next
            
            self.tail = prev
            prev.next = None

        self.length -= 1
            
        return temp


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(4)
linked_list.pop()
linked_list.print_list()
linked_list.pop()
linked_list.print_list()
linked_list.pop()
linked_list.print_list()
