class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None # Creates an empty tree


    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                temp = temp.right 
                return True

            else: # if its on the left side:
                if temp.left is None:
                    temp.left = new_node
                temp = temp.left

                return True
            

    def contains(self, value):
        # if self.root is None:
        #     return False
        
        temp = self.root
        while temp is not None:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left

            else:
                return True
            
        return False
            

                    



            
my_tree = BinarySearchTree()
my_tree.insert(4)
my_tree.insert(7)
my_tree.insert(1)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)



        





    