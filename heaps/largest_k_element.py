import heapq

class KthLargest(object):
    """
    Finds the kth largest element in a stream using a min heap of size k.
    
    Key Insight: The kth largest element is the SMALLEST among the k largest elements.
    By maintaining exactly k elements in a min heap, heap[0] is always the kth largest.
    """

    def __init__(self, k, nums):
        """
        Initialize with k (the rank to track) and initial numbers.
        
        Time: O(n * log k) where n = len(nums)
        Space: O(k)
        """
        self.k = k
        self.heap = []  # Min heap to store k largest elements
        
        # Add all initial numbers to heap
        for n in nums:
            heapq.heappush(self.heap, n)
        
        # Keep only k largest by removing smallest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        """
        Add new value to stream and return the kth largest element.
        
        Time: O(log k)
        Space: O(1)
        
        Returns:
            int: The kth largest element after adding val
        """
        # Always push the new value
        heapq.heappush(self.heap, val)
        
        # If heap exceeds size k, remove the smallest
        # This ensures we only keep the k largest elements
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # Root of min heap = smallest of k largest = kth largest overall
        return self.heap[0]


# Example usage:
# obj = KthLargest(3, [4, 5, 8, 2])
# obj.add(3)  # Returns 4 (3rd largest among [4, 5, 8, 2, 3])
# obj.add(5)  # Returns 5 (3rd largest among [4, 5, 8, 2, 3, 5])
# obj.add(10) # Returns 5 (3rd largest among [4, 5, 8, 2, 3, 5, 10])
