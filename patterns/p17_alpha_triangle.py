rows = 5
for i in range(rows):
    # Part 1: Spaces
    print(" " * (rows - i - 1), end="")

    # Part 2: Left Half (A, AB, ABC...)
    for k in range(i + 1):
        print(chr(ord('A') + k), end="")

    # Part 3: Right Half (mirror)
    for k in range(i - 1, -1, -1):
        print(chr(ord('A') + k), end="")

    print()
