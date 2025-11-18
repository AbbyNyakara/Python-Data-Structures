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

        return new_node

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
        dummy1.make_empty()

        dummy2 = LinkedList(2)
        dummy2.make_empty()

        current = self.head

        while current is not None:
            if current.value < x:
                dummy1.append(current.value)
            else:
                dummy2.append(current.value)
            current = current.next

        # Now we have 2 partitions: (Connect the 2)
        dummy2_head = dummy2.head
        dummy1.tail.next = dummy2_head
        dummy2.head = None  # detach

        self.head = dummy1.head
        self.tail = dummy2.tail


linked_list = LinkedList(5)
linked_list.append(9)
linked_list.append(3)
linked_list.append(4)
linked_list.append(2)
linked_list.append(1)
linked_list.partition_list(2)
linked_list.print_list()
