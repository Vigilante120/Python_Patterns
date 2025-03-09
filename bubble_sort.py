unsorted = [30, 25, 55, 95, 5]


for i in range(len(unsorted) -  1):
    if unsorted[0] < unsorted[1]:
        unsorted[0] = unsorted[1]

print(unsorted)