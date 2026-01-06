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

    def contains(self, value):
        temp = self.root 
        while temp is not None:
            if value < temp.value:
                temp = temp.left # jump to left node it will move the head down.
            elif value > temp.value:
                temp = temp.right # jump to right node it will also move the head down towards right.
            else:
                return True
        return False
    
    


            


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(27))
print(my_tree.contains(17))