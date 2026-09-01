def funcThree():
    print("three")

def funcTwo():
    funcThree()
    print("Two")

def funcOne():
    funcTwo()
    print("one")

funcOne()

