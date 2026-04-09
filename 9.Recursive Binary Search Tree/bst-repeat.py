class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_value(self, value):
        new_node = Node(value)

        # TODO 1 - If the BST is completely empty 
        if self.root is None:
            self.root = new_node

        # TODO 2 - If it contains a value 
        current_node = self.root 

        while True: 
            if value == current_node.value:
                return False # cannot contain duplicates
            
            if value < current_node.value:
                if current_node.left is not None:
                    current_node = current_node.left
                current_node.left = new_node
                return True

            elif value > current_node.value:
                if current_node.right is not None:
                    current_node = current_node.right
                current_node.right = new_node
                return True
            
    def contains(self, value):
        if self.root is None: # if the tree is empty definitely does not contain the number: 
            return False
        
        temp = self.root
        
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else: # value == temp.value
                return True
        return False # got to temp = None and the value 




new_bst = BinarySearchTree()
new_bst.insert_value(47)
new_bst.insert_value(23)
new_bst.insert_value(53)

print(new_bst.root.value)
print(new_bst.root.left.value)
print(new_bst.root.right.value)
        
print(new_bst.contains(47))
        

        