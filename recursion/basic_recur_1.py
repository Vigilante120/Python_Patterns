# creating a countdown

def countdown(cnt):
    if cnt == 0:
        return True

    print(cnt)
    countdown(cnt - 1)

countdown(10)