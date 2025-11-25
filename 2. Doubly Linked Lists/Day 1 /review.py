class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
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
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            temp = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.prev = temp

        self.length += 1

    def pop(self):
        '''
        # Edge cases : empty list, 1 node and multiple
        Removes a node from the end of a dounle linked list
        '''

        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
        return temp

    def pop_first(self):
        '''
        Removes the Node at the beginning of a LinkedList
        '''
        if self.head is None:
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
        return temp

    def prepend(self, value):
        '''
        Adds a node to the beginnig of a linked List
        Edge cases - Empty / 1 or more 
        '''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return new_node

    def get(self, index):
        '''
        Retrieves a node at a certain index of a Double Linked list

        :param self: Description
        :param index: The Index of the Linked List
        p:s - For this case, we can start from the front or the back depending on the idx we are
        trying to fetch
        '''
        if index < 0 or index >= self.length:  # Means its out of range
            return None
        else:
            if index < self.length/2:
                temp = self.head  # start from the front
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail  # start from the tail
                for _ in range(self.length-1, temp, -1):
                    temp = temp.prev
            return temp
        
        


linked_list = DoubleLinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
print(linked_list.get(2))


# linked_list.print_list()
