def reverse_between(self, start_index, end_index):

        if self.length < 2 or start_index == end_index:
            return
    
        dummy = Node(0)
        dummy.next = self.head
        s