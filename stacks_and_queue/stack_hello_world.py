
stack = [] 
close_to_open = { 
    ')': '(', 
    ']': '[', 
    '}': '{' 
}

s = "()[]{}"

stack = []

for char in s:
    if char in close_to_open:
        print(close_to_open[char])
for char in s:
    if char in close_to_open:
        if stack and stack[-1] == close_to_open[char]:
            stack.pop()
        else:
            print(False) 
    else:
        stack.append(char)

if len(stack) == 0:
    print(True)
else:
    print(False)
        