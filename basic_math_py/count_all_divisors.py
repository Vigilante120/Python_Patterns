def divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


print(divisors(12))

# counted all divisors!! always remember put return outside of loop!!