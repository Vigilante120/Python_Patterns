

# here we will prep for a job interview 

# we will hunt list and dict stuff first 

from collections import deque
import heapq
"""
Method A: Using zip() (Two lists)
If you have one list for keys and another for values, zip() is the cleanest approach.
"""
keys = ['name', 'framework', 'language']
values = ['Nishant', 'Django', 'Python']
mydict = list(zip(keys, values))
print(mydict)

"""
Method B: List of Tuples
If your list already contains paired elements (which is very common when parsing scraped data), you can cast it directly using dict().
"""
paired_list = [('name', 'Nishant'),  ('framework', 'django')]
mydict = dict(paired_list)
print(mydict)


"""
DICT COMPREHENSION
"""
my_list = [1,2,3,4]

sqr_dict = {x: x**2 for x in my_list}
print(sqr_dict)

cube_dict = {x: x**3 for x in my_list}
print(cube_dict)

"""
LIST COMPREHENSION
[expression for item in iterable if condition]

expression: What you want to do to the item (e.g., multiply it, uppercase it, or just keep it as is).

for item in iterable: The standard loop part.

if condition: (Optional) A filter to only include certain items.
"""

square_list = [x**2 for x in my_list]
print(square_list)

cube_list = [x**3 for x in my_list]
print(cube_list)

name_list = ["nishant", "vikram", "ben"]

cap_name = [x.capitalize() for x in name_list]
print(cap_name)


"""
simple for loop
"""

for i in range(1, 6):
    print(i)


"""
access items in list
"""

locations = ["Chandigarh", "Delhi", "Bangalore"]
i  =  1
for loc in locations:
    print(f"Location_{i}:", loc)
    i += 1


for i in range(5, 0, -1):
    print(i)

# division is decimal by def
print("new division")
print(5 / 2)

language = "Python"

for x in language:
    print(x, end=" ")

print()

queue = deque()
queue.append(1)
queue.append(2)
print(queue)


queue.pop()
queue.appendleft(0)
print(queue)

# hashset 

mySet = { i for i in range(5) }
print(set(mySet))

# dict | hashmap 
"""
myMap.keys() gives only the keys.
myMap.values() gives only the values.
myMap.items() gives both key and value pairs.


Functions of Dict 

Read: get(), keys(), values(), items().
Change: update(), setdefault().
Delete: pop(), popitem(), clear().
Copy/create: copy(), fromkeys().

"""
myMap = {}
myMap['Alice'] = 25
myMap['Nishant'] = 26
print(myMap)

# looping through the dict 

for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)

# tuples are like arrays but immutable

"""
helper functions 

# creation
t = (1, 2)
t = tuple(iterable)

# access
t[i]

# built-in helpers
len(t)
min(t)
max(t)
sum(t)

# tuple methods
t.count(x)
t.index(x)

# membership
x in t
x not in t

# dictionary usage
d[(1, 2)] = value

# set usage
s.add((1, 2))
(1, 2) in s

"""
tup = (1, 2, 3)
print(tup)
if tup[0]== 1:
    print(True)
else:
    print(False)


myMap_2 = { (1,4): 3 }
print(myMap_2[(1,4)])

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)


s = set()
s.add((1,2))
print(s)


minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

print(minHeap[0], "\n")

while len(minHeap):
    print(heapq.heappop(minHeap))

class MyClass:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)