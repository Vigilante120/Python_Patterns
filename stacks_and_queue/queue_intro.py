"""
Queue Data Structure Documentation

Introduction:
    A Queue is a linear data structure that follows the First In First Out (FIFO) principle.
    This means that the first element added to the queue will be the first one to be removed.
    It is conceptually similar to a line of people waiting for a service; the person who arrives
    first is served first.

Key Characteristics:
    1. FIFO (First In First Out): The element inserted first is the first one to be deleted.
    2. Ordered List: Elements are stored in a specific sequence based on arrival.
    3. Two Ends:
        - Front (Head): The end from where elements are removed (dequeued).
        - Rear (Tail): The end where elements are added (enqueued).

Common Operations:
    - Enqueue: Adds an item to the rear of the queue.
      Time Complexity: O(1)
    
    - Dequeue: Removes an item from the front of the queue.
      Time Complexity: O(1)
    
    - Peek/Front: Returns the item at the front without removing it.
      Time Complexity: O(1)
    
    - IsEmpty: Checks if the queue is empty.
      Time Complexity: O(1)
    
    - Size: Returns the number of items in the queue.
      Time Complexity: O(1)

Implementation Approaches:
    1. Arrays (Lists):
       Simple to implement but removing from the beginning (index 0) can be inefficient (O(n))
       because all subsequent elements must be shifted.
    
    2. Linked Lists:
       Efficient O(1) for both enqueue and dequeue operations. We maintain pointers to both
       the head (first) and tail (last) nodes.
    
    3. Collections.deque:
       Python's built-in double-ended queue is highly optimized for appending and popping
       from both ends.

Applications:
    - CPU Scheduling: Managing processes waiting for CPU time.
    - Data Buffers: IO buffers, CD player buffers, streaming.
    - Print Spooling: Documents waiting in line to be printed.
    - Breadth-First Search (BFS): Used in graph traversal algorithms to explore neighbors."""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node

        else:
            self.last.next = new_node
            self.last = new_node
        
        self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1 
        return temp
            
        

my_queue = Queue(1)
my_queue.enqueue(2)

my_queue.dequeue()
my_queue.print_queue()