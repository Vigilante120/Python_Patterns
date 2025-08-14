
def armstrong(n):
    number = str(n)
    raised_to_pwr = len(number)
    sum_ = 0

    for i in number:
        sum_ += int(i) ** raised_to_pwr

    # print(sum_)
    if sum_ == n:
        return True
    else:
        return False

print(armstrong(153))
# Armstrong number is a number that is equal to the sum of its digits
# each raised to the power of the number of digits in the number.
# For example, 153 is an Armstrong number because
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

"""
step 1 = calculate the length of n
step 2 that len of n will be the power of each number
step 3 after that add all the numbers and return the sum if sum == n 
the num is armstrong! """