# start = 1 , N = value

def num_print(start, end):
    if start > end:
        return

    print(start)
    num_print(start + 1, end)

num_print(1, 10)