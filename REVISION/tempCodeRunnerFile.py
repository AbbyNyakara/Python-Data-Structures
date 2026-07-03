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