class Node:
    def __init__(self, value):
        self.value = value
        # There are nodes pointing both ways
        self.next = None
        self.prev = None


class DoublyLinkedList:
    '''
    Creates a Doubly Linked List
    '''

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
        '''
        Adds a node to the End of a Doubly linked List
        '''
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

    def pop(self):
        '''
        Removes a node from the end of linked List
        '''
        if self.head is None:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
            return None
        else:
            temp = self.tail

            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

            self.length -= 1
            return temp

    def prepend(self, value):
        '''Adds a Node to the beginning of a linkedList'''
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        '''Removes a Node from the beginning of a linked List. Please Note that the oorder matters'''
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp.value


double_linked_list = DoublyLinkedList(2)
double_linked_list.append(1)
print(double_linked_list.pop_first())
print(double_linked_list.pop_first())
print(double_linked_list.pop_first())
