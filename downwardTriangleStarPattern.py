def pattern12(rows):
    # Initial number of spaces in row 1
    spaces = 2 * (rows - 1)

    # Outer loop for the number of rows
    for i in range(1, rows + 1):
        # Printing numbers in ascending order in each row
        for j in range(1, i + 1):
            print(j, end="")

        # Printing spaces in each row
        for j in range(1, spaces + 1):
            print(" ", end="")

        # Printing numbers in descending order in each row
        for j in range(i, 0, -1):
            print(j, end="")

        # Move to the next line after printing each row
        print()

        # Decrease the number of spaces by 2 after each row
        spaces -= 2


if __name__ == "__main__":
    rows = 5
    pattern12(rows)
