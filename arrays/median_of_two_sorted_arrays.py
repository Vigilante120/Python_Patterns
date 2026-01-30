
def find_median(nums1, nums2):
    
    merged = sorted(nums1 + nums2)
    n = len(merged)
    
    mid = n // 2

    if n % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2.0
    else:
        return float(merged[mid])

nums1 = [1,2]
nums2 = [3,4]
print(find_median(nums1, nums2))