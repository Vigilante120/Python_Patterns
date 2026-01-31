from collections import deque

people = ["Dante", "Vergil", "Leon", "Chris"]

people = deque(people)

people.append("Ada")
people.appendleft("Ashley")
print(people)
people.popleft()
print(people)
print("---")
people.rotate(-1)
print(people)

help(deque)