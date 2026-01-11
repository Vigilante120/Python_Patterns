# this code find duplicates inside the code
def find_duplicates(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    duplicates = []
    for num, count in counts.items():
        if count > 1:
            duplicates.append(num)
    return duplicates


    

print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )
