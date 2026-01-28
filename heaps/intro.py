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
