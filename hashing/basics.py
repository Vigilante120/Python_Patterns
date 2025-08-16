arr = [1, 4, 6, 3, 4, 4, 2]
hash_table = {}

# Precompute counts
for num in arr:
    if num in hash_table:
        hash_table[num] += 1
    else:
        hash_table[num] = 1

print(hash_table)
