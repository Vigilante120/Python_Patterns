rows = 5
s = "ABCDE"
for i in range(rows):
    for j in range(rows - i):
        print(s[j], end="")
    print()