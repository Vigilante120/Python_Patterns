def contains_nearby_duplicate(nums, k):
    seen = {}  # This dictionary stores {number: last_seen_index}

    for i in range(len(nums)):
        current_num = nums[i]

        # 1. Check if the number is in our dictionary
        if current_num in seen:
            # 2. Check if the distance between current index 'i' 
            # and the previous index is <= k
            if i - seen[current_num] <= k:
                return True
        
        # 3. Update the dictionary with the current index
        # If the number exists, we overwrite the old index with the new one
        seen[current_num] = i
    
    return False

# --- Test Examples ---

# Example 1: True (The 1s are at index 0 and 3. Distance is 3. k=3)
print(f"Example 1: {contains_nearby_duplicate([1, 2, 3, 1], 3)}") 

# Example 2: True (The 1s are at index 0 and 1. Distance is 1. k=1)
print(f"Example 2: {contains_nearby_duplicate([1, 0, 1, 1], 1)}")

# Example 3: False (The 1s are at index 0 and 3. Distance is 3. But k=2)
print(f"Example 3: {contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2)}")