class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root

        while True:
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left 


            elif value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


            else: # value == temp.value:
                return False

    def contains(self, value):
        if self.root is None:
            return False
        
        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left

            elif value > temp.value:
                temp = temp.right 

            else: # temp == temp.value
                return True
            
        return False

bst = BinarySearchTree()

print(bst.insert(47))   # True
print(bst.insert(21))   # True
print(bst.insert(76))   # True
print(bst.insert(21))   # False
print(bst.insert(76))   # False
print(bst.insert(47))   # False

print("Check contains logic")
print(bst.contains(200))


