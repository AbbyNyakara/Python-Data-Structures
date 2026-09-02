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
        if self.root == None:
            self.root = new_node

        temp = self.root
        while True:
            if value > temp.value:
                if temp.right is not None:
                    temp = temp.right
                    return True
                temp.right = new_node

            elif value < temp.value:
                if temp.left is not None:
                    temp = temp.left
                    return True
                temp.left = new_node

            else:
                return False  # if value == any node's value

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

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False

        if value == current_node.value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)

        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    

    def __r_insert(self, current_node, value):
        pass


    def r_insert(self, value):
        self.__r_insert(self.root, value)


my_tree = RecursiveBinarySearchTree()
my_tree.insert(23)
my_tree.insert(45)
my_tree.insert(12)

print(my_tree.root.right.value)

print(my_tree.r_contains(11))
