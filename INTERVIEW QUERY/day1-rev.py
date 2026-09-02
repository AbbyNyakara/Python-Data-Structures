class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


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
            if value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
            # else:
                temp = temp.right

            elif value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

            else:
                return False

    def contains(self, value):

        if self.root is None:
            return False

        temp = self.root

        while True:
            if value < temp.value:
                if temp.left is not None:
                    temp = temp.left
                else:
                    return False

            elif value > temp.value:
                if temp.right is not None:
                    temp = temp.right
                else:
                    return False

            else: # if value == temp.value
                return True


bst = BinarySearchTree()
bst.insert(23)
bst.insert(12)
bst.insert(34)
bst.insert(11)


# print(bst.root.value)
# print(bst.root.left.value)
# print(bst.root.right.value)
print(bst.contains(34))
