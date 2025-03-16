def bubble(n):
    swapped = False
    while not swapped:
        swapped = True
        for i in range(0, len(n)-1):
            if n[i] > n[i+1]:
                swapped = False
                n[i], n[i + 1] = n[i+1], n[i]
    return n


unsorted = [5,4,3,2,1]

print(bubble(unsorted))

"""
Input: You pass an unsorted list (unsorted =) to the bubble() function.

Initialization:
A variable swapped is set to False initially. This variable is meant to track whether any swaps happen during a pass through the list.

Outer Loop:
The while not swapped: loop runs until no swaps are made in a complete pass through the list.
Inside this loop, swapped is set to True at the beginning of each pass.

Inner Loop:
The for loop iterates over the indices of the list (from 0 to len(n)-2) and compares each pair of adjacent elements (n[i] and n[i+1]).
If the first element in the pair (n[i]) is greater than the second (n[i+1]), they are swapped.

Return: Once the list is sorted, it exits the loop and returns the sorted list.
"""