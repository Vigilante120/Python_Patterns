
def box(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end='')
            else:
                print(' ', end="")
        print()



box(5)


"""
**** 

*  *

*  *

****

deduced that first and last line have all the stars 
2,4,6 are blank / empty
3, 5 are filled but with only 
i should be
"""