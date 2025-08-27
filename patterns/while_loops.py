numbers = [1, 10, 20, 35, 55]
search_num = 20
index = 0

while index < len(numbers):
    if numbers[index] == search_num:
        print(f"{search_num} found at index {index}")
        break
    index += 1
else:
    print(f"{search_num} not found in the list")