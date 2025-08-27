def print18(n):
    for i in range(n):
        # ord[E] = 69 starting point, ord[A] = 65 Ending
        # but E is at the last always means at the end is ord[E]
        # rest is getting pushed before E
        starting = ord('A') + n - 1 - i
        ending = ord('A') + n - 1
        # print(f"starting point = {starting} | ending point =  {ending}")

        for code in range(starting, ending + 1):
            print(chr(code), end=" ")
        print()

print18(5)