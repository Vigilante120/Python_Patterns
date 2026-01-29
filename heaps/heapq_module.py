"""
The heapq module is Python's built-in implementation of the heap queue algorithm (also known as the priority queue algorithm), which provides efficient methods for managing min heaps. It works directly on regular Python lists without requiring a custom class.
"""

"""
Essential Operations
heappush(heap, item): Adds an element to the heap while maintaining the heap property

heappop(heap): Removes and returns the smallest element from the heap

heapify(list): Transforms an existing list into a valid heap in-place

heapreplace(heap, item): Pops the smallest item and then pushes a new item (more efficient than separate operations)

heappushpop(heap, item): Pushes an item then pops the smallest (more efficient than separate calls)
"""

"""
nsmallest(n, iterable): Returns a list with the n smallest elements

nlargest(n, iterable): Returns a list with the n largest elements

merge(*iterables): Merges multiple sorted inputs into a single sorted output
"""

import heapq

# creating a heap from scratch 
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
print(heap)

# popping the smallest elements 
smallest = heapq.heappop(heap)
print(smallest)
print(heap)


# converting an list to a heap
nums = [20, 1, 5, 12, 9]
print(f"before heap conversion{nums}")
heapq.heapify(nums)
print(f"after heap conversion{nums}")

# FIFO Heapq means heap Queue and its implement for priority queues

"""
Patterns:
Finding k largest/smallest elements: When you need to track only the top k items efficiently

Priority-based processing: When elements need to be processed by priority rather than arrival order

Streaming data: When elements arrive continuously and you need to maintain sorted access to extremes (min/max)

Merge sorted sequences: Combining multiple sorted streams efficiently

Shortest path algorithms: Like Dijkstra's where you repeatedly need the minimum distance node


"""