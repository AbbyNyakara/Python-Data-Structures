'''
You are given a singly linked list that contains integer values, 
where some of these values may be duplicated.

Your task is to implement a method called remove_duplicates()
 within the LinkedList class that removes all duplicate values from the list.

Your method should not create a new list, but rather modify the 
existing list in-place, preserving the relative order of the nodes.
'''


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
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next

    def remove_duplicates_nested_loop(self):
        # The current and the runner set at the head:
        current = self.head

        while current is not None:
            print(f"checking duplicates for {current.value}")
            previous = current
            runner = previous.next

            while runner is not None:  # runner is a node
                if runner.value == current.value:  # im comparing the values here
                    previous.next = runner.next  # remove the duplicate the move it to the other node
                    runner = runner.next
                    # Note: previous stays where it is!
                else:
                    previous = runner
                    runner = runner.next

            current = current.next
            


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(4)
linked_list.append(5)
linked_list.append(1)
linked_list.append(6)
linked_list.append(2)
linked_list.remove_duplicates_nested_loop()

linked_list.print_list()
