from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        length = 0
        has_odd = False
        # we need a algorithm to find out how we are going to reverse and find the longest palindrome 

        for count in counts.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd = True
            
        return length + 1 if has_odd else length