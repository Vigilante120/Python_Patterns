def longest_con_seq(nums):
    num_set = set(nums)
    longest = 0 

    for n in nums:

        if (n - 1) not in num_set:
            length = 1
    
            while (n + length) in num_set:
                length += 1
            
        longest = max(length, longest)
        
    return longest



print(longest_con_seq([100, 4, 200, 1, 3, 2]))



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""