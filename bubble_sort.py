unsorted = [30, 25, 55, 95, 5]

for i in range(len(unsorted)):
    for j in range(len(unsorted) - i - 1):
        if unsorted[j] > unsorted[j + 1]:
            unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]

print(unsorted)
