
def uniqChar(s):
    count = {}

    # going through the string
    for char in s:
        count[char] = count.get(char, 0) + 1

    # lookup now using hashmap
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
        
    return -1

s = "banana"

print(uniqChar(s)) # output index will be 0