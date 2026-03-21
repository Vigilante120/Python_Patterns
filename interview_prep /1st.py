# here we will prep for a job interview 

# we will hunt list and dict stuff first 

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
    