rows = 4
space = 4
s = "ABC"
for i in range(rows):
    for j in range(space - i): # spaces
        print(" ", end="")

    for j in range(i): # values
        print("#", end="")

    for j in range(i, 1, -1): # values #2
        print(s[j], end="")

    print()

