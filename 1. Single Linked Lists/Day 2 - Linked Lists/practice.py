class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        '''Initialize / Create a new linked list'''
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        The append method should add a new node with a given value to 
        the end of the linked list, updating the tail attribute and the
        length attribute accordingly.

        Should work for an empty list O(1)
        """
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = None

        self.length += 1

    def pop(self):
        """
        The pop method should remove the last node (tail) from the linked 
        list and return the removed node. 

        If the list is empty, the method should return None.
        """
        # The case that its empty:
        if self.length == 0:
            return None

        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next

            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
                self.head = None

            return temp

    def prepend(self, value):
        '''
        The prepend method should add a new node with a given value to the 
        beginning of the linked list, updating the head attribute and the 
        length attribute accordingly.
        '''

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp

        self.length += 1

    def pop_first(self):
        """
        The pop_first method should remove the first node (the head) 
        from the linked list, update the head attribute and the length
        attribute accordingly, and return the removed node.

        """

        if self.length == 0:
            return None  # Nothing to see

        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1

            if self.length == 0:  # becomes empty after removing:
                self.head = None
                self.tail = None

        return temp

    def get(self, index):
        '''
        The get method should take an integer index as a 
        parameter and return a pointer to the node at 
        the specified index in the linked list.O(n)
        '''
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        """
        The set_value method should take an integer index and a value 
        as parameters and update the value of the node at the specified 
        index in the linked list.
        """
        if index < 0 or index >= self.length:
            return False

        target_node = self.get(index)
        target_node.value = value

        return True

    def insert(self, index, value):
        """
        The insert method should take an integer index and a value as
        parameters and insert a new node with the given value at the 
        specified index in the linked list.
        """
        new_node = Node(value)
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        prev = self.get(index-1)  # This retrieves the node before the target.

        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        The remove method should take an integer index as a parameter 
        and remove the node at the specified index in the linked list,
        returning the removed node.
        """
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index-1)
        target = temp.next  # That is the target node to be removed:
        temp.next = target.next
        target.next = None
        self.length -= 1
        return target

    def reverse(self):
        """
        The reverse method should reverse the order of the nodes 
        in the linked list so that the head becomes the tail 
        and the tail becomes the head.
        """
        # Reassign the head and the tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # Now create the variables
        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before  # Flip the arrow:
            before = temp
            temp = after


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.reverse()

linked_list.print_list()
