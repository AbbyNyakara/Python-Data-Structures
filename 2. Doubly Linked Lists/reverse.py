class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        # empty or has nodes
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    def print_vals(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next

    def reverse_list(self):
        temp = None
        current = self.head

        # Reverse the direction of the arrows
        while current is not None:
            next_node = current.next # store this here coz it will get changed

            current.next = current.prev 
            current.prev = next_node
            
            temp = current
            current = next_node

        self.tail = self.head
        self.head = temp
        


new_ll = DoublyLinkedList(1)
new_ll.append(2)
new_ll.append(3)
new_ll.reverse_list()
new_ll.print_vals()
