# value , left , right 
# simple constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None # BST FIRST u dont add the root value at the time u create the class instead we will use insert function to initialize the code
        # the perfect constructor

    def insert(self, value):
        #TC: if root = None, root = new_node ;) 
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True # we will break out here as the root is freshly produced
        temp = self.root
        while (True):
            if new_node.value == temp.value: # we are comparing the values here so we are using(.value)
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

            


my_tree = BinarySearchTree()
print(my_tree.insert(2))
print(my_tree.insert(1))
print(my_tree.insert(3))

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)