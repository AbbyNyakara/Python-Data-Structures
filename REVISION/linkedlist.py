class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        '''
        Appends a node to the end of a linked list
        '''
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

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
        ''' 
        Removes a node at the end of a linkedList and returns the node

        - Empty List
        - One node
        - More than one node
        '''

        if self.head is None:
            return None

        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
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

    def prepend(self, value):
        '''
        Add a node at the beginning of a linked list 

        - empty
        - More than 1 
        '''

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
            self.length += 1

        return True


linkedlist = LinkedList(1)
linkedlist.append(12)
linkedlist.append(17)
linkedlist.prepend(34)
linkedlist.prepend(2)
linkedlist.print_list()
