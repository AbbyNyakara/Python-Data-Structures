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

    def pop(self):
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
        if self.head is None:  # if the list is empty
            self.append(value)
        else:
            temp = self.head
            new_node = Node(value)
            self.head = new_node
            self.head.next = temp
            self.length += 1


list = LinkedList(2)
list.pop()
list.prepend(45)


print(list.head.value)

# print(list.pop())
# print(list.pop())
# print(list.pop())
# print(list.pop())
