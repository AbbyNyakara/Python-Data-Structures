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
                for _ in range(self.length-1, index, -1):
                    temp = temp.prev
            return temp
        
    def set_value(self, index, value):
        '''
        It sets the value of a node at a certain index
        
        :param self: Description
        :param index: Index in which to set/ change the value the value
        :param value: the new value
        '''
        target_node = self.get(
            index)  # This can be none if the index is out of range:
        if target_node:  # is not None
            target_node.value = value

            return True
        return False

    def insert(self, index, value):
        '''
        Insert a Node at a specific index with a certain value
        
        :param self: Description
        :param index: the index to insert at
        :param value: The value of the node
        '''
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False

        if index == 0:
            # This is wrong! append and prepend accept a value and not a new_node
            self.prepend(new_node)
        if index == self.length:
            self.append(new_node)

        prev = self.get(index-1)  # Could result to None

        # The node before the actual position and the actual position
        if prev is not None and prev.next is not None:
            target_node = prev.next
            new_node.next = target_node
            prev.next = new_node
            target_node.prev = new_node
            new_node.prev = prev
        self.length += 1
        return True

    # def remove(self, index):
    #     '''
    #     Removes a node from a LinkedList at a certain index

    #     :param self: Description
    #     :param index: Description
    #     '''

    #     if index < 0 or index >= self.length:
    #         return None
    #     if index == 0:
    #         return self.pop_first()
    #     if index == self.length-1:
    #         return self.pop()
    #     else:
    #         prev = self.get(index-1)  # Retrieves the Node at the prev index
    #         target = self.get(index)
    #         after = target.next
    #         target.next = None
    #         target.prev = None
    #         after.prev = None
    #         after.prev = prev
    #         prev.next = None
    #         prev.next = after
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        return temp




    
linked_list = DoubleLinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.remove(3)


linked_list.print_list()
