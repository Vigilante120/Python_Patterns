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


## two sum 

def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))

for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

inter = []
for n in intervals:
    inter.extend(n)

print(inter)

def merge_intervals(intervals):
   
    intervals.sort(key=lambda x: x[0])
    merged = []

    for current in intervals:
        if not merged or current[0] > merged[-1][1]:
           merged.append(current)
        else:
            merged[-1][1] = max(merged[-1][1], current[1])
    return merged

data = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(data))

# recursion 

def factorial(n):
    # base case 
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(996))

def fibo(n):
    if n == 0 or n == 1:
        return n
    
    return fibo(n - 1) + fibo(n -2)

for i in range(10):
    print(fibo(i), end=" ") 
