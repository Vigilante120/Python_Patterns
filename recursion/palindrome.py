# arr , # original , start, end

def palin_check(arr, start, end, original):
    if start >= end:
        if arr == original:
            return True
        else:
            return False

    arr[start], arr[end] = arr[end], arr[start]
    return palin_check(arr, start + 1 , end - 1, original)


arr = [1,2,3,4,5]
original = arr[:]

result = palin_check(arr, 0, len(arr)- 1, original)
print("Result", result)
