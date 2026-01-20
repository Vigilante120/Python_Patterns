class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        left = 0 
        res = 0

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            
            seen[char] = right 
            res = max(res, right - left + 1)

        return res