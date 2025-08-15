# start end as usual
def rev_rec(arr, start, end):
    if start >= end:
        return
    # else:
    arr[start], arr[end] = arr[end], arr[start]
    rev_rec(arr, start + 1, end - 1)

arr = [5,4,3,2,1]
print("Original array: ", arr)

rev_rec(arr, start = 0, end = len(arr) - 1)
print("Reversed Array: ", arr)
