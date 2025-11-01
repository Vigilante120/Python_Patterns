class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=' ')
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.tail
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
            new_node = Node(value)
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            self.length += 1
            return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head 
        
        if self.length == 1:
            self.head = None
            self.tail = None
        # in this logic i just shifted my head to next as 
        # the problem is popping first 
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1 
        return temp
        
        




my_dll = DoublyLinkedList(7)
my_dll.pop_first()
my_dll.print_list()
