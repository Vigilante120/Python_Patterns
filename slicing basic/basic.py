"""
In Python, slicing is a way to extract parts of sequences like:
list
tuple
string
"""

"sequence[start:stop:step]"

"""
Meaning:
start → index where slicing begins (inclusive).
stop → index where slicing ends (exclusive).
step → how many elements to skip between each item.

If you skip something:
start defaults to 0 (start of sequence).
stop defaults to len(sequence) (end of sequence).
step defaults to 1 (no skipping).
"""

word = "PYTHON"
print(word[-1])
print(word[-2])

# BASIC SLICING EXAMPLE
print(word[0:4]) # START FROM 0 end at 3rd index
print(word[:4]) # Start from default end at 4th index
print(word[2:]) # Start From Two End at default
print(word[:]) # 'PYTHON' (full copy)

# STEP PARAM
print(word[::2]) #PTO printed every 2nd character
print(word[1::2]) # start from Y then step by 2 YHN

# NEGATIVE INDEXING
print(word[-4:-1]) # start from last 4 to last THO [-1] will not be printed
print(word[-4:]) # start from 4th index end at default

# Lists using Slicing
nums = [10,20,30,40,50,]
print(nums[1:4]) # start at 20 end at 40
print(nums[::-1]) # reverse everything

# MODIFYING LISTS USING SLICING
nums[1:3] = [99, 100]
print(nums)

nums[::2] = [1, 2, 3]
print(nums)

# ADVANCED SLICING PATTERNS
word = "ABCDEFGHIJ"
print(word[2:8:3]) # CF
print(word[-8:-2:2]) # CEG

# 10. Slicing rules to remember
# Exclusive stop → stop is never included.
# Out of range indexes are fine → Python won't throw an error:
print(word[2:99])



