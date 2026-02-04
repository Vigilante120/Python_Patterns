nums = [1,2, 3,4] # list

squared = list(map(lambda x: x**2, nums))
print(squared)

"""
map() applies a function to EACH element of an iterable and returns the results.

In plain English:

“Take every item, run it through this function, collect the outputs.

input list  →  function  →  output list

"""

nums1 = [4, 5, 6, 7]

cubed = list(map(lambda x: x**3, nums1))
print(cubed)

"""
map function explained 
map(function, iterable)
"""

x1 = [421, 553, 66, 67, 21, 90]

def make_even(num):
    if num % 2 == 1:
        return num + 1
    else:
        return num

x2 = list(map(make_even, x1))
print("map function in action", x2)


