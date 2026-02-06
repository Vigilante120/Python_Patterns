# 2d Lists
matrix = [[1,2,3], [4,5,6], [7,8,9]]

rows, cols = 3,4 

# matrix = [[2 for j in range(cols) for i in range(rows)]]
# print(matrix)

# using indices 
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=' ')
    print()

# direct iteration
for row in matrix:
    print(end='\n')
    for element in row:
        print(element, end=' ')
print()



#           --COLUMNS--
fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
#.           <--------------ROW----------->
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
print(groceries)

print(groceries[1][1])

for row in groceries:
    for food in row:
        print(food, end=" ")
    print()

# for row in groceries:
#     for element in row:
#         print(element, end=" ")

print("New Exercises")
# tuple is faster than list

num_pad = ([1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"])


for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()
print("Practice time")

def spirtal_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # dir 1
        for col in range(left, right + 1):
            res.append(matrix[top][col])
        top += 1
        # dir 2
        for row in range(top, bottom + 1):
            res.append(matrix[row][right])
        right -= 1
        # dir 3 move left along bottom row
        if top <= bottom:
            for col in range(right, left - 1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1
        # dir 4
        if left <= right:
            for row in range(bottom, top - 1, -1):
                res.append(matrix[row][left])
            left += 1
            
        
        return res

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spirtal_matrix(matrix))

print("looping in reverse")

# range(start, stop, step)
for i in range(10, 0, -1):
    print(i)

# to reverse list
print("reverse a list using reverse method")
nums = [4,3,2,1]
for i in reversed(nums):
    print(i, end= " ")

print("reverse through index")
# reverse through index

nums = [10,20,30,40]
for i in range(len(nums) - 1, - 1, -1):
    print(nums[i])

# reverse string s

s = "python"
for char in range(len(s) -1, -1, -1):
    print(s[char], end="")
print()

s = "I love coding"
for char in range(len(s)- 1, -1 , -1):
    print(s[char], end="")

print("\nprinting even numbers in reverse")

n = 10 
for i in range(n, 0, -1):
    if i % 2 == 0:
        print(i)

print("\nReverse index")

arr = [5, 15, 25]

for i in range(len(arr) -1 , -1, -1):
    print(f"Index: {i} Value: {arr[i]}")

# reverse pattern 

print("Reverse Pattern")
n = 4 
for i in range(n, -1, -1):
    print("*" * i)


n = 12345

while n > 0:
    r = n % 10 
    print(r, end="")
    n = n // 10 # this is just a breaking statement


print(" Checking the // symbol ")
a = 43
# a = a // 10
# print(a)
# a = a // 10
# print(a)

# base case while loop 0 pr lekr ana hai 
# iterative case usme humne remainder

while a > 0:
    remainer = a % 10
    print(remainer, end="")
    # exit case 
    a = a // 10 

print("Checking %")
b = 552
print(b % 10)

c = 1000

while c > 0:
    r = c % 10
    print(r, end="")
    c = c // 10
