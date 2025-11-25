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

    def remove_duplicates(self):  # 0(N)
        vals = set()
        current = self.head
        previous = None

        while current is not None:
            if current.value in vals:
                previous.next = current.next

            else:
                vals.add(current.value)
                previous = current

            current = current.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(4)
linked_list.append(5)
linked_list.append(1)
linked_list.append(6)
linked_list.append(2)
linked_list.remove_duplicates()
linked_list.print_list()
