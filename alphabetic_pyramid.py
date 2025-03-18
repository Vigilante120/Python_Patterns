# Define the string of characters to be used in the triangle
values = "ABCDE"

# Define the initial number of spaces for alignment
# This value ensures the triangle is right-aligned
spaces = 4

# Outer loop: Iterate through each row of the triangle
for i in range(0, len(values)):
    # First inner loop: Print spaces to align the triangle to the right
    # The number of spaces decreases as 'i' increases
    for j in range(spaces - i):
        print(" ", end="")  # Print a space without moving to the next line

    # Second inner loop: Print the letter corresponding to the current row
    # The letter is repeated (i + 1) times in each row
    for j in range(i + 1):
        print(values[i], end=' ')  # Print the letter with a space after it

    # Move to the next line after finishing the current row
    print()