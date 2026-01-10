def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False



list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1, list2)) # 5 is common in here 

# above method is O(n square)
# now making it into a Dict [HashTable]

def items_in_common(l1, l2):
    my_dict = {}
    for i in l1:
        my_dict[i] = True
    
    for j in l2:
        if j in my_dict:
            return True
    
    return False

print(items_in_common(l1=list1, l2=list2)) # O(N)

