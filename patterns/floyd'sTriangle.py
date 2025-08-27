rows = 5
count = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()

"""
Explanation of Code Components: 📌
rows = 5: Specifies the number of rows in the triangle.

count = 1: Initializes the starting number for the sequence.

Outer Loop (for i in range(1, rows + 1):):

Controls the number of rows.

i represents the current row number.

Inner Loop (for j in range(i):):

Runs i times for each row, ensuring that each row has an increasing number of elements (1 element in the first row, 2 in the second, etc.).

print(count, end=" "):

Prints the current value of count on the same line with a space separating numbers.

count += 1:

Increments count so that the next number is printed in sequence.

print():

Moves to a new line after completing each row.
"""