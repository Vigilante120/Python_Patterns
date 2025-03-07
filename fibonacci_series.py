series  = [0 , 1]
for i in range(10):
    series.append(series[-1] + series[-2])
    result = series

print(series)

"""series[-1]: Refers to the last element in the series list.

series[-2]: Refers to the second-to-last element in the series list.

series[-1] + series[-2]: Adds these two elements to generate the next number in the Fibonacci sequence."""