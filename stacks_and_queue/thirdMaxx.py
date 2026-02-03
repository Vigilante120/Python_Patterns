class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))

        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]