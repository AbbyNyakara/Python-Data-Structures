class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class RecursiveBinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        current = self.root
        if value < current.value:
            while current.left is not None:
                current = current.left
            current.left = new_node
            return True

        if value > current.value:
            while current.right is not None:
                current = current.right
            current.right = new_node
            return True
        
        if value == current.value:
            return False
        
    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        
        elif value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
        else: #value == current_node.value:
            return True
        
        
        

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


        
my_tree = RecursiveBinarySearchTree()

my_tree.insert(47)
my_tree.insert(40)
my_tree.insert(52)

print(my_tree.root.left.value)
