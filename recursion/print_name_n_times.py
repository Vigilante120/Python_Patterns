# n = end
# i = start

def print_names(start, end):
    if start > end:
        return

    print("Nishant")
    print_names(start + 1, end)

print_names(1, 10)