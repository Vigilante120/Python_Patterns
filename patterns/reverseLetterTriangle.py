values = "ABCDE"

for i in range(0, len(values)):
    for j in range(i + 1):
        print(values[i], end=" ")
    print()