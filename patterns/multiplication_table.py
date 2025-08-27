

table = int(input("Enter the number whose table you want to print: "))
if table < 0:
    print("Value is less than 0")
else:
    for i in range(1, 11):
        print(f"{table} * {i} = {table * i}")

"""
for loop: Iterates through numbers from 1 to 10 (inclusive).

range(1, 11): Generates a sequence of numbers starting at 1 and ending at 10.
"""