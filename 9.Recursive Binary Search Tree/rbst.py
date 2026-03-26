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

        temp = self.root

        while True:
            if value == temp.value:
                return False

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

    # def __r_insert(self, current_node, value):
    #     if current_node == None:
    #         return Node(value)

    #     if value < current_node.value:
    #         current_node.left = self.__r_insert(current_node.left, value)
    #     if value > current_node.value:
    #         current_node.right = self.__r_insert(current_node.right, value)

    # def _r_insert(self, value):
    #     if self.root == None:
    #         self.root = Node(value)
    #     self.__r_insert(self.root, value)

    def contains(self, value):
        if self.root is None:
            return False

        temp = self.root

        while temp is not None:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True
        return False

   


my_tree = RecursiveBinarySearchTree()
my_tree.insert(47)
my_tree.insert(23)
my_tree.insert(61)
# my_tree.insert(19)
# my_tree.insert(34)
# my_tree.insert(50)
# my_tree.insert(72)

# print(my_tree.root.left.value)


