rows = 5
for i in range(1, rows):
    for j in range(1, i + 1):
        print(j , end="")

    for j in range(2 * (rows - i - 1)): # why this formula ?
# we need 6 spaces and to achieve that we need to do some math magic
# 2 * (5 - 1 - 1) = 2 * 3 = 6 hence, 6 spaces will be created :)
            print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()