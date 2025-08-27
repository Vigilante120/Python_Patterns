
def triangle(n):
    spaces = 0
    for i in range(n):
        # star
        for j in range(n - i):
            print("*", end="")
        # spaces
        for j in range(spaces):
            print(" ", end="")
        # right stars
        for j in range(n - i):
            print("*", end="")

        spaces += 2
        print()

        # lower half the formula created is by seeing that the beginning
        # is from the max spaces so we can use
        # spaces = 2 * n - 2 i.e 8 spaces then reduce by 2 each round of loop

    spaces = 2 * n - 2
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        for j in range(spaces):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        spaces -= 2
        print()

triangle(5)