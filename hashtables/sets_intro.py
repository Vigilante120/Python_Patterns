"""
Sets are similar to dictionaries except that instead of having key/value pairs they only have the keys but not the values.

Like dictionaries, they are implemented using a hash table (which is why we are covering them here).

Sets can only contain unique elements (meaning that duplicates are not allowed). 

they are useful for various operations such as finding the distinct elements in a collection and performing set operations such as union and intersection.

They are defined by either using curly braces {} or the built-in set() function like this:

"""

# create a set using {}
my_set = {1,2,3,4,5}
my_set = set([1,2,3,4,5])

# we can add an element to a set 

my_set.add(6)

# Update is used to add multiple elements to the set at once. 
# It takes an iterable object (e.g., list, tuple, set) as an 
# argument and adds all its elements to the set. 
# If any of the elements already exist in the set, 
# they are not added again.

my_set.update([3,4,5,6])

# removing an element off of set

my_set.remove(3)

# ===== UNION, INTERSECTION, AND DIFFERENCE EXPLAINED =====

# Let's use simple examples to understand these operations
students_math = {"Alice", "Bob", "Charlie", "David"}
students_science = {"Bob", "David", "Eva", "Frank"}

print("Math students:", students_math)
print("Science students:", students_science)
print()

# 1. UNION - Combines all unique elements from both sets
# Think of it as "Who takes EITHER math OR science (or both)?"
union_result = students_math.union(students_science)
# Alternative way: union_result = students_math | students_science

print("UNION - All students taking math OR science:")
print(union_result)
# Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'}
print("Total students:", len(union_result))
print()

# 2. INTERSECTION - Only elements that exist in BOTH sets
# Think of it as "Who takes BOTH math AND science?"
intersection_result = students_math.intersection(students_science)
# Alternative way: intersection_result = students_math & students_science

print("INTERSECTION - Students taking BOTH math AND science:")
print(intersection_result)
# Output: {'Bob', 'David'}
print("Students taking both subjects:", len(intersection_result))
print()

# 3. DIFFERENCE - Elements in first set but NOT in second set
# Think of it as "Who takes math but NOT science?"
difference_result = students_math.difference(students_science)
# Alternative way: difference_result = students_math - students_science

print("DIFFERENCE - Students taking math but NOT science:")
print(difference_result)
# Output: {'Alice', 'Charlie'}
print()

# Let's try the reverse difference
reverse_difference = students_science.difference(students_math)
print("Students taking science but NOT math:")
print(reverse_difference)
# Output: {'Eva', 'Frank'}
print()

# ===== MORE PRACTICAL EXAMPLES =====

# Example 1: Food preferences
likes_pizza = {"John", "Mary", "Tom", "Sarah"}
likes_burgers = {"Mary", "Tom", "Mike", "Lisa"}

print("=== FOOD PREFERENCES ===")
print("Likes pizza:", likes_pizza)
print("Likes burgers:", likes_burgers)

# Who likes at least one of these foods?
food_lovers = likes_pizza | likes_burgers  # Using | operator for union
print("Likes pizza OR burgers:", food_lovers)

# Who likes both foods?
both_foods = likes_pizza & likes_burgers  # Using & operator for intersection
print("Likes BOTH pizza AND burgers:", both_foods)

# Who likes only pizza (not burgers)?
only_pizza = likes_pizza - likes_burgers  # Using - operator for difference
print("Likes ONLY pizza:", only_pizza)
print()

# Example 2: Programming languages
knows_python = {"Alex", "Sam", "Jordan", "Casey"}
knows_java = {"Sam", "Jordan", "Taylor", "Morgan"}

print("=== PROGRAMMING LANGUAGES ===")
print("Knows Python:", knows_python)
print("Knows Java:", knows_java)

# All programmers
all_programmers = knows_python.union(knows_java)
print("All programmers:", all_programmers)

# Multi-language programmers
multi_lang = knows_python.intersection(knows_java)
print("Knows both Python and Java:", multi_lang)

# Python-only programmers
python_only = knows_python.difference(knows_java)
print("Knows only Python:", python_only)

# Java-only programmers
java_only = knows_java.difference(knows_python)
print("Knows only Java:", java_only)
print()

# ===== MEMORY TIP =====
print("=== MEMORY TIPS ===")
print("UNION (|): Brings everything together - like a big group photo")
print("INTERSECTION (&): Only what's common - like shared interests")
print("DIFFERENCE (-): What's unique to the first group - like exclusive members")
print()

# Working with the original sets from earlier
other_set = {3,4,5,6}
union_set = my_set.union(other_set)

# Intersection of two sets
intersection_set = my_set.intersection(other_set)
 
# Difference https://www.w3schools.com/python/python_sets.asp between two sets
difference_set = my_set.difference(other_set)
 
# Checking if an element is in a set
if 1 in my_set:
    print("Found hello in my_set")


# union example 

numbers = [1,1,2,3,4]
first = set(numbers)
second = {1, 5}

print(first | second) # union 
print(first & second) # finds the common [Intersection = Common]
print(first - second) # difference, numbers that are different in both lists

if 1 in first:
    print('yes 1 is present') # in short SETS IS AN UNORDERED COLLECTION OF UNIQUE ELEMENTS 
    