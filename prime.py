
def prime(n):
    if n <= 1:
        return False
    # will use square root here so n ** .5
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


print(prime(10**10+7))

# space complexity is 0(1) time complexity 0(root n)