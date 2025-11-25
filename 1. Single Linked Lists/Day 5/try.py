
"""
remove duplicates

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.tail = new_node
        self.head = new_node

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

        while current is not None:
            print(current.value)
            current = current.next

    def remove_duplicates(self):
        current = self.head
        runner = self.head

        while current is not None:
            previous = current
            runner = current.next
            while runner is not None:
                if runner.value == current.value:
                    previous.next = runner.next
                    runner = runner.next
                else:
                    previous = runner
                    runner = runner.next
                current = current.next


linked_list = LinkedList(1)
linked_list.print_list()
