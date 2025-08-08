rows = 5
s = "ABCDE"
for i in range(rows):
    for j in range(i + 1):
        print(s[j], end="")
    print()
