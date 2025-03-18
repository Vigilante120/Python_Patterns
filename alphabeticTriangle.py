# Define the string of characters to be used in the triangle
values = "ABCDE"

# Outer loop: iterate through the indices of the 'values' string
for i in range(len(values)):
    # Inner loop: iterate from 0 to i (inclusive)
    for j in range(i + 1):
        # Print the character at index j, followed by a space
        # This prints characters from the beginning of 'values' up to the i-th position
        print(values[j], end=" ")
    # Move to the next line after completing each row
    print()

