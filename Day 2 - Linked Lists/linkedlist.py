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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Method appends Node to the END of a LinkedList

        If the LinkedList is empty, set the head and tail as the new node
        else, if set thetail to the new node
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop_last(self):
        """
        
        """
        if self.length == 0:
            return None  # Nothing to pop
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:  # if this is true
                pre = temp
                temp = temp.next  # move the temp over..
            # when temp.next is None ( I am at the last NOde:)
            self.tail = pre
            self.tail.next = None
            self.length -= 1

            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value

    def prepend(self, value):
        """
        Add a new node at the beginning of a linkedList
        """
        new_node = Node(value)
        if self.length == 0:  # if the list is empty
            self.head = new_node
            self.tail = new_node
        else:  # If list has something in it:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        self.length += 1

    def pop_first(self):
        """
        Pops the first node from the linkedList
        """
        # If it is empty:
        # if there is only 1 node in
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None  # to disconnect it from the chain: ie. its pointing to none/nothing

        self.length -= 1
        if self.length == 0:  # when we have
            self.tail = None
        print(f"The head value is {self.head.value}")
        return temp

    def get(self, index):
        """
        Returns the node at a certain index
        Case 1 - Empty LinkedList
        Case 2 - Can fetch the index # The indx will start from 0:
        Case 3 - The index is out of range: # if I have reached the tail 
        """
        # Case 1: Empty List , if it is outside the range:
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set_value(self, index, value):
        """
        Sets the value of a certain Node in a linkedList. 
        """
        temp = self.get(index)
        # This will return a Node ( with next and Value or None)

        if temp:  # if tremp is not none:
            temp.value = value
            return True

    def remove_node(self, index):
        """Removes a node at a certain index"""
        if index < 0 or index >= self.length:  # In the case that the index is out of range:
            return None

        if index == 0:
            self.pop_first()

        if index == self.length - 1:
            self.pop_last()

        prev = self.get(index-1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None

        self.length -= 1

        return temp

    def reverse(self):
        if self.length == 0:
            return None
        if self.length == 1:
            pass  # Do nothing:

        # Switch them
        temp = self.head
        self.head = self.tail
        self.tail = temp

        while temp.next is not None:
            temp = temp.next  # Until I get to the last Node:

        self.head = temp  # when temp.next is none
        self.tail = self.head








list = LinkedList(11)
list.append(3)
list.append(23)
list.append(7)
list.set_value(1, 4)


list.print_list()
