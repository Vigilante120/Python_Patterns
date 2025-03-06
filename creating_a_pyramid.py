#pyramid
rows = 5

# assigning outer loop
for i in range(rows):
    #assigning Spaces
    for j in range(rows - i - 1):
        print(" ", end='')
    # assigning stars *
    for j in range(i + 1):
        print("*", end=' ')
    print()
"""
We start by setting the number of rows we want in our pyramid. In this case, it's 5.

The program then goes through each row, one by one, from top to bottom.

For each row, it does two main things:
a) First, it prints some spaces. The number of spaces decreases as we go down the pyramid.
b) Then, it prints some stars. The number of stars increases as we go down the pyramid.

After printing the spaces and stars for a row, it moves to the next line to start the next row.

This process repeats for all 5 rows.
"""