# Count from 1 to 10
count = 1
while count <= 10:
    print(count)
    count += 1

## while loop using user input
user_input = ""
while user_input != "quit":
    user_input = input("Enter a command ( type 'quit' to exit): ")
    print("You entered:", user_input)

print("Program Ended")


## using break statement

number = 1
while True:
    if number == 5:
        break
    print(number)
    number += 1
print("Loop ended")