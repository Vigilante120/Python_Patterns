
rows = 5

for i in range(rows):
    if i < rows - 1:
        print("*")
    else:
        print("* " * rows)

"""
The condition if i < rows - 1: ensures that all rows except the last one print a single *.

The last row (i == rows - 1) prints *** to form the horizontal base of the "L".

You can adjust the value of rows to change the size of the "L".
"""