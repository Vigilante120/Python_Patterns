def isPossibleToSplit(nums):
    seen = {} 
    nums1 = []
    nums2 = []
    # create a frequency map 
    for n in nums:
        seen[n] = seen.get(n, 0) + 1

    
    # append the frequency of 1 to other lists
    for element, frequency in seen.items():
        if frequency > 2:
             return False

        elif frequency == 2:
            nums1.append(element)
            nums2.append(element)

        elif frequency == 1:
            if len(nums1) > len(nums2):
                nums2.append(element)
            else:
                nums1.append(element)
        
        
    return len(nums1) + len(nums2) == len(nums)

nums = [1,1,2,2,3,4]

print(isPossibleToSplit(nums))