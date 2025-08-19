numbers = [1, 3, 2, 1, 3, 3, 2]


count_dict = {}

for number in numbers:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

for key in count_dict:
    print(f"{key} appears {count_dict[key]} times ")
