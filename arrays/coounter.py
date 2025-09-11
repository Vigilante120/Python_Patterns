arr1 = [1, 2, 2, 3, 4]
arr2 = [2,2,3,5]

freq = {}

for num in arr1:
    freq[num] = freq.get(num, 0) + 1

common = {}
for num in arr2:
    if freq.get(num, 0) > 0:
        common[num] = common.get(num, 0) + 1
        freq[num] -= 1


print(list(common.values()))




