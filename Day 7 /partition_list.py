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
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next

    def make_empty(self):
        """Empties the ll"""
        self.head = None
        self.tail = None

    def partition_list(self, x: int):
        # Empty:
        if self.head is None:
            return

        dummy1 = LinkedList(1)
        dummy1.make_empty()  # I dont have to create one to make empty

        dummy2 = LinkedList(2)
        dummy2.make_empty()

        current = self.head

        while current is not None:
            if current.value < x:
                dummy1.append(current.value)
            else:
                dummy2.append(current.value)
            current = current.next

        # Handle the case where dummy 1 is empty
        if dummy1.head is None:
            self.head = dummy2.head
            self.tail = dummy2.tail
        elif dummy2.head is None:
            self.head = dummy1.head
            self.tail = dummy1.tail

        else:
            dummy2_head = dummy2.head
            dummy1.tail.next = dummy2_head
            dummy2.head = None
            self.head = dummy1.head
            self.tail = dummy2.tail


linked_list = LinkedList(5)
linked_list.append(9)
linked_list.append(3)
linked_list.append(4)
linked_list.append(2)
linked_list.append(1)
linked_list.make_empty()
linked_list.partition_list(4)
linked_list.print_list()
