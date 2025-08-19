# leet code 509

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib = [0, 1]
            for i in range(2, n + 1):
                fib.append(fib[i - 1] + fib[i - 2])
            return fib[n]