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

        # Create a temp value to point to the root
        temp = self.root
        while temp is not None:
            if new_node.value < temp.value:
                if temp.left is None:  # There is no node there
                    temp.left = new_node
                    return True
# There's a node
                temp = temp.left

            elif new_node.value == temp.value:
                return False
            else:  # new_node.value > temp.value

                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False

        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left 
            elif value > temp.value:
                temp = temp.right
            else: # value == temp.value
                return True
        return False


bst = BinarySearchTree()
bst.insert(42)
bst.insert(32)
bst.insert(70)

print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
print("-----------")
print(bst.contains(42))