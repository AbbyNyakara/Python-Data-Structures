'''
Write a method called partition_list(self, x) that rearranges the nodes in a doubly linked 
list so that all nodes with a value less than a given number x come before all nodes with a 
value greater than or equal to x.

You must maintain the original relative order of the nodes in each of the two partitions.

The partitioning must be performed in-place. You cannot create new nodes (other than dummy nodes).

Both .next and .prev pointers must be updated correctly.

If the list is empty, nothing should happen.

🧪 Examples
Example 1
Input DLL:
3 <-> 8 <-> 5 <-> 10 <-> 2 <-> 1
Partition value: x = 5
Output DLL:
3 <-> 2 <-> 1 <-> 8 <-> 5 <-> 10

Why:
Nodes < 5: 3, 2, 1
Nodes >= 5: 8, 5, 10
Order of nodes is preserved in both groups
Smaller group comes before larger/equal group

Example 2
Input DLL:
1 <-> 2 <-> 3
Partition value: x = 5
Output DLL:
1 <-> 2 <-> 3
Why:
All nodes are already less than x. No rearrangement needed.

Example 3
Input DLL:
7 <-> 8 <-> 9
Partition value: x = 5
Output DLL:
7 <-> 8 <-> 9
Why:
All nodes are >= x. Order remains the same.

Example 4
Input DLL:
1
Partition value: x = 2
Output DLL:
1
Why:
Single-node list. Nothing to rearrange.

Example 5
Input DLL:
(empty)
Partition value: x = 3
Output DLL:
(empty)
Why:
Empty list. Nothing to do.
'''


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

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def append(self, value):
        # Completely empty ll
        # There's atleast 1 node
        # 0(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def partition_list(self, x):
        if not self.head:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)

        # Create the pointers
        less = dummy1
        greater = dummy2

        # Traverse the list
        current = self.head
        while current is not None:
            nxt = current.next
            current.prev = None
            current.next = None
            if current.value < x:
                less.next = current
                current.prev = less
                less = current
            else:
                greater.next = current
                current.prev = greater
                greater = current
            current = nxt
        # 2 detached lists
        if dummy2.next is not None: 
            less.next = dummy2.next
            dummy2.next.prev = less

            self.head = dummy1.next
            self.tail = greater

        else:
            self.head = dummy1.next
            self.tail = less

        self.head.prev = None
        self.tail.next = None
            



new_dll = DoublyLinkedList(3)
new_dll.append(8)
new_dll.append(5)
new_dll.append(10)
new_dll.append(2)
new_dll.append(1)
# new_dll.print_list()
new_dll.partition_list(5)
new_dll.print_list()
