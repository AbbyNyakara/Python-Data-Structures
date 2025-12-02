

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
        while current:
            print(current.value)
            current = current.next

    def decode(self):
        # Read the values in each node
        result = 0
        current = self.head

        while current is not None:
            result *= 2
            node_value = current.value
            result += node_value
            current = current.next
        return result


linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(0)
print(linked_list.decode())

# print(linked_list.decode())
