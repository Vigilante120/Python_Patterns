# The GCD (Greatest Common Divisor) is the largest number
# that divides two or more numbers without leaving a remainder
def gcd(n1, n2):
    if n2 > n1:
        # mini = minimum
        mini = n1
    else:
        mini = n2

    hcf = None
    for i in range(1, mini + 1):
        if n1 % i == 0 and  n2 % i == 0:
            hcf = i
    print(f"GCD of {n1} & {n2} = {hcf}")

gcd(54352392, 2312323342)

