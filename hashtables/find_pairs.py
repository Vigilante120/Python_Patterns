def find_pairs(arr1, arr2, target):
    # a + b = target we gonna do b = target - a
    set2 = set(arr2)
    pairs = []

    for num in arr1:
        b = target - num

        if b in set2:
            pairs.append((num, b))
    return pairs


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""