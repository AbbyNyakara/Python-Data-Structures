"""
DLL: Swap Nodes in Pairs ( ** Interview Question)
ATTENTION: Advanced Doubly Linked List Challenge Ahead!
This question is acknowledged as one of the more intricate challenges within the Doubly Linked List section. It's not unusual for students to find this task quite formidable at this point in the course.
If you're considering diving into this problem, it's crucial to approach it methodically. I recommend drawing out the list structures and operations to better visualize the problem. This challenge demands a deep understanding of Doubly Linked Lists' unique characteristics and manipulation techniques.
Use this opportunity to deepen your understanding, but also remember it's absolutely fine to come back to this problem later if it feels overwhelming now. Progress in complex concepts like these sometimes requires stepping back and revisiting with fresh insights. Good luck, and remember that perseverance is key in mastering these advanced topics!
Now, here is the problem:
You are given a doubly linked list.
Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.
Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.
Example:
1 <-> 2 <-> 3 <-> 4 should become 2 <-> 1 <-> 4 <-> 3
Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.
Note: You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)
"""
# The DLL does not have a tail

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value=value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value=value)
        
        
        # if empty
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

        self.length += 1
        return True
    
    def print_list(self):
        """Print the values in the dll"""
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next

    def swap_pairs(self):
        if self.length in (0,1):
            return
        
        dummy = Node(0)
        dummy.next = self.head # helps track the head
        self.head.prev = dummy
        
        # pointer
        temp = dummy
        first = temp.next
        
        while first and first.next:
            second = first.next
            # Detach the node
            first.next = second.next
            if second.next:
                second.next.prev = first

            # Swap the nodes
            temp.next = second
            second.prev = temp

            second.next = first
            first.prev = second

            temp = first
            first = temp.next

        # The head:
        self.head = dummy.next
        self.head.prev = None # detach the dummy 

dll = DoubleLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.swap_pairs()

dll.print_list()

                
            

        




