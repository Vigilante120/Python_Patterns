
nums = [9,6,4,2,3,5,7,0,1]

n = len(nums)

expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

print(expected_sum - actual_sum)

