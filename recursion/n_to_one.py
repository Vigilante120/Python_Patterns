# start , goal = 1

def n_to_one(start):
    if start < 1:
        return

    print(start)
    n_to_one(start - 1)

n_to_one(10)
