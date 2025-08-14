from math import log10

def count(n):
    cnt = int(log10(n)) + 1
    return cnt

print(count(121))