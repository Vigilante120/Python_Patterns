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

my_tree = BinarySearchTree()
print(my_tree.root) # this will print None :) 
