values = "ABCDE"

# length of value is 4 and we want it to go till 0 by decrementing the original value by 1
for i in range(len(values), 0, -1):
    # now we know i value is currently at 4 so we call i value in j so that it decrement automatically
    for j in range(i):
        print(values[j], end=" ")
    print()