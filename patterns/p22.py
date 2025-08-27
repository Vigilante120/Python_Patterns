def numbox(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            # need to calc dist from all the sides
            # top = i, left = j, bottom = size - 1 - i, right= size-1-j
            min_distance = min(i, j, size - 1 - i, size - 1 - j)
            value = n - min_distance
            print(value, end=" ")
        print()


numbox(6)
##