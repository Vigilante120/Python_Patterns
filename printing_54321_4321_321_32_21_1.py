
rows = 5
columns = 5
for i in range(0, rows + 1):
    for j in range(columns - i, 0, -1):
        print(j, end=' ')
    print()



"""rows = 5 and columns = 5: These set the dimensions of our pattern.
for i in range(0, rows + 1):: This is the outer loop that iterates from 0 to 5 (6 iterations).

for j in range(columns-i, 0, -1):: This is the inner loop that:
    Starts from columns-i (which decreases with each row)
    Ends at 1 (since 0 is excluded in range())
    Steps backwards (-1 step)
    # NOTE = range(start, stop, step) means in the inner loop we started from 4 we going till 0 and we be decrementing
    the value for that's why outer loop is used. 

print(j, end=' '): This prints the current value of j followed by a space.
print(): After each inner loop completes, this moves to a new line."""