class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):

        new_node = Node(value) # step 1 - create the Node

        if self.root is None:
            self.root = new_node # if the root is not there, the node becomes the root 
            return True # Exit the code: 

        current = self.root

        while True:
            if new_node.value == current.value:
                return False
            
            if new_node.value < current.value: 
                if current.left is not None:
                    current = current.left
                current.left = new_node
                return True

            if new_node.value > current.value:
                if current.right is not None:
                    current = current.right
                current.right = new_node
                return True
            
    def contains(self, value):
        if self.root is None:
            return False
        
        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            elif value == temp.value:
                return True
            
        return False


        
bst = BinarySearchTree()    
bst.insert(47)
bst.insert(21)
bst.insert(76)
print(bst.contains(21))



            

        