rows = 5
for i in range(rows):
    if i % 2 == 0:
        start = 1
    else:
        start = 0

    val = start

    for j in range(i + 1):
        print(val, end=" ")
        val = 1 - val
    print()