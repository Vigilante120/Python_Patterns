"""
Python zip() Function Demonstrations

This module showcases different ways to use Python's built-in zip() function:
1. Creating dictionaries from separate lists
2. Parallel iteration over multiple sequences
3. Unpacking/unzipping paired data

The zip() function takes multiple iterables and returns an iterator of tuples
where each tuple contains elements from all iterables at the same index.
"""

# Example 1: Creating a dictionary from separate lists using zip()
print("=== Example 1: Creating Dictionary from Lists ===")
keys = ['name', 'age', 'job']
values = ['Nishant', 25, 'Engineer']

# zip() pairs each key with its corresponding value
# dict() constructor converts the zip object to a dictionary
user_data = dict(zip(keys, values))
print(f"User data dictionary: {user_data}")
print(f"Type: {type(user_data)}\n")

# Example 2: Parallel iteration over multiple lists
print("=== Example 2: Parallel Processing/Iteration ===")

# Three lists with soccer player statistics
players = ["Striker", "Midfielder", "Defender"]
goals = [12, 5, 2]
cards = [1, 3, 0]

print("Player Statistics:")
print("-" * 40)
# zip() allows iterating through all three lists simultaneously
# Each iteration gives us one element from each list at the same position
for p, g, c in zip(players, goals, cards):
    print(f"Position: {p:10} | Goals: {g:2} | Yellow Cards: {c}")

print()

# Example 3: Unpacking/Unzipping data using zip(*iterable)
print("=== Example 3: Unpacking Pairs with zip(*iterable) ===")

# List of tuples (paired data)
pairs = [('a', 1), ('b', 2), ('c', 3)]
print(f"Original pairs: {pairs}")

# zip(*pairs) unpacks the list of tuples
# The * operator unpacks the list, so zip gets: ('a', 1), ('b', 2), ('c', 3)
# zip() then groups the first elements together and second elements together
letters, numbers = zip(*pairs)

print(f"Extracted letters: {list(letters)}")
print(f"Extracted numbers: {list(numbers)}")
print(f"Letters type: {type(letters)}")
print(f"Numbers type: {type(numbers)}")

# Additional example: What happens with unequal length lists
print("\n=== Additional: Behavior with Unequal Lengths ===")
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y']

# zip() stops at the shortest list
result = list(zip(list1, list2, list3))
print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"List3: {list3}")
print(f"Zip result: {result}")
print("Note: zip() stops when the shortest iterable is exhausted")