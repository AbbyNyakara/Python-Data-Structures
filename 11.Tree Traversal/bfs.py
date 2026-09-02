"""
Breadth first search is where we traverse through the BST

"""


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

        temp = self.root

        while True:
            if value == temp.value:
                return False
            if value < temp.value:
                if temp.left is not None:
                    temp = temp.left
                    return True
                temp.left = new_node

            elif value > temp.value:
                if temp.right is not None:
                    temp = temp.right
                    return True
                temp.right = new_node

    def contains(self, value):
        if self.root is None:
            return False

        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left

            elif value > temp.value:
                temp = temp.right

            else:  # value == temp.value
                return True

        return False
    
    def breadthFirstSearch(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return result


bst = BinarySearchTree()
bst.insert(47)
bst.insert(21)
bst.insert(76)
bst.insert(18)


# print(bst.root.value)
# print(bst.root.left.value)
# print(bst.root.right.value)

print(bst.breadthFirstSearch())
