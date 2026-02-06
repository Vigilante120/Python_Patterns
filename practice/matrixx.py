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