


def butterfly(n):
    space = 2 * n - 2
    #upper triangle
    for i in range(n):

        # left starts
        for j in range(i + 1):
            print("*", end="")
        for j in range(space):
            print(" ",end="")
        for j in range(i + 1):
            print("*", end="")
        space -= 2
        print()
    space = 2
    for i in range(1, n):
        # left stars
        for j in range(n - i):
            print("*", end="")
        # space
        for j in range(space):
            print(" ", end="")
        # right *
        for j in range(n - i):
            print("*", end="")
        space += 2
        print()

butterfly(5)

#easiest shit
