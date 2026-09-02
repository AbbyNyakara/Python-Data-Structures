class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        '''
        Appends a node to the end of a linked list
        '''
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop(self):
        ''' 
        Removes a node at the end of a linkedList and returns the node

        - Empty List
        - One node
        - More than one node
        '''

        if self.head is None:
            return None

        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        else:
            prev = None
            temp = self.head

            while temp.next is not None:
                prev = temp
                temp = temp.next

            self.tail = prev
            prev.next = None
            self.length -= 1
            return temp

    def prepend(self, value):
        '''
        Add a node at the beginning of a linked list 

        - empty
        - More than 1 
        '''

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
        
        self.length += 1
        return True

    def pop_first(self):
        '''
        Removes the first node from the linkedlist and returns it 
        '''
        if self.length == 0:
            return None

        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def get(self, index):
        if index < 0 or index > self.length - 1:
            return None
        if index == 0:
            return self.head
        if index == self.length - 1:
            return self.tail
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next

            return temp
        

    def set(self, index, value):
        """
        Sets the value of a node at a certain index
        """
        selected_node = self.get(index) #this could result in none if index is not valid

        if selected_node is not None:
            selected_node.value = value
            return True
        return False
    

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.prepend(value)
            
        if index == self.length:
            return self.append(value)

        # Create a new node
        new_node = Node(value)

        before = None
        temp = self.head

        for _ in range(index):
            before = temp
            temp = temp.next

        new_node.next = temp
        before.next = new_node

        self.length += 1

        return True

    def remove(self, index):
        if index < 0 or index > self.length - 1:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length -1:
            return self.pop()
        
        # Removing from the middle: 

        before = None
        temp = self.head

        for _ in range(index):
            before = temp
            temp = temp.next 

        before.next = temp.next 
        temp.next = None

        self.length -= 1


    def reverse(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return None
        
        before = None
        temp = self.head
        self.head = self.tail
        self.tail = temp

        while temp is not None:
            after = temp.next

            temp.next = before
            before = temp
            temp = after

        return True

        

linkedlist = LinkedList(1)
linkedlist.pop()
linkedlist.append(12)
linkedlist.append(17)
linkedlist.append(5)
linkedlist.print_list()
linkedlist.reverse()
print("After Reversal")
linkedlist.print_list()


