# making a frequency nap 

# counts = {number : frequency}
nums = [3,2,3]
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
print(counts)



list_1 = [10, 20, 30, 30, 20]
counts_dict = {}

for num in list_1:
    counts_dict[num] = counts_dict.get(num, 0) + 1
print(counts_dict)

# we created two frequency maps above now time to check the map

n = len(nums)

for k, v in counts.items():
    if v > n / 2:
        print(k)


def majority_element(nos):
    counts = {}
    n = len(nos)
    
    # 1. THE BUILD (Perfect)
    for num in nos:
        counts[num] = counts.get(num, 0) + 1
    
    # 2. THE CHECK
    # We use (key, value) to separate the Number from its Count
    for num, count in counts.items():
        if count > n / 2:
            return num  # Found it!
            
    return None # If no majority exists

print("Majority Elements\n")

nos = [10,10,20,30]
print(majority_element(nos))

# enumerate example 

a = "apple"

for i,char in enumerate(a):
    print(i, char)
print()



student_list = {
    "nishant": 90,
    "muskaan": 95,
    "somil": 100
}


for name, percentage in student_list.items():
    print(f"Name: {name.capitalize()}, Percentage(%): {percentage}")