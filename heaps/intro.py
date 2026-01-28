class MaxHeap:
    """
    A Max Heap implementation where the parent node is always greater than or equal to its children.
    The largest element is always at the root (index 0).
    Uses a complete binary tree structure stored as an array/list.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty max heap.
        
        The heap is represented as a list where:
        - Index 0 contains the root (maximum element)
        - Elements are filled level by level, left to right
        """
        self.heap = []  # Empty list to store heap elements


    def _left_child(self, index):
        """
        Calculate the index of the left child of a node.
        
        Args:
            index (int): The index of the parent node
            
        Returns:
            int: The index of the left child
            
        Formula: For a node at index i, left child is at 2*i + 1
        Example: Parent at index 0 → left child at index 1
        """
        return 2 * index + 1
    
    
    def _right_child(self, index):
        """
        Calculate the index of the right child of a node.
        
        Args:
            index (int): The index of the parent node
            
        Returns:
            int: The index of the right child
            
        Formula: For a node at index i, right child is at 2*i + 2
        Example: Parent at index 0 → right child at index 2
        """
        return 2 * index + 2
    
    
    def _parent(self, index):
        """
        Calculate the index of the parent of a node.
        
        Args:
            index (int): The index of the child node
            
        Returns:
            int: The index of the parent node
            
        Formula: For a node at index i, parent is at (i-1)//2
        Example: Child at index 1 or 2 → parent at index 0
        Uses integer division (//) to discard remainder
        """
        return (index - 1) // 2


    def _swap(self, index1, index2):
        """
        Swap two elements in the heap.
        
        Args:
            index1 (int): Index of the first element
            index2 (int): Index of the second element
            
        Used during heap operations to maintain the max heap property
        when elements need to be rearranged.
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    

    def _insert(self, value):
        # bubble up
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and
                self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
            
            if (right_index < len(self.heap) and
                self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
    
    

    

        



myheap = MaxHeap()
myheap._insert(99)
myheap._insert(75)
myheap._insert(80)
myheap._insert(55)
myheap._insert(60)
myheap._insert(50)
myheap._insert(65)

print(myheap.heap)
myheap.remove()
print(myheap.heap)

myheap.remove()
print(myheap.heap)
