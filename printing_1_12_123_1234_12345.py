row = 5
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

"""This code creates a pattern of numbers in a triangular shape. Here's how it works:

row = 5: This sets the number of rows for the pattern.

for i in range(1, row + 1):: This is the outer loop that iterates from 1 to 5 (since row + 1 is 6).

for j in range(1, i + 1):: This is the inner loop that iterates from 1 to the current value of i.

print(j, end=''): This prints the current value of j without moving to a new line (due to end='').

print(): After each inner loop completes, this moves to a new line."""