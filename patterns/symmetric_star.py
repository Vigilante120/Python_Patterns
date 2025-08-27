rows = 5

# Increasing rows
for i in range(1, rows + 1):
    print("x " * i)

# Decreasing rows
for i in range(rows - 1, 0, -1):
    print("x " * i)
"""
📌 Explanation of Logic
The first loop (range(1, rows + 1)) prints an increasing number of stars (*) from 1 up to rows (5 in this case).

The second loop (range(rows - 1, 0, -1)) prints a decreasing number of stars from rows - 1 down to 1.
"""