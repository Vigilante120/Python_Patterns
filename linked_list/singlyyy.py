# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
# # head -> tail
#
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def display(self):
#         elements = []
#         current_node = self.head
#         while current_node:
#             elements.append(str(current_node.data))
#             current_node = current_node.next
#         print(" -> ".join(elements))
#
#     def append(self, data):
#         new_node = Node(data)
#
#         if self.head is None:
#             self.head = new_node
#             return
#
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#
#         last_node.next = new_node
#
# # sll = SinglyLinkedList()
# # print("Initial List:")
# # sll.display()
# #
# # sll.append(10)
# # sll.append(20)
# # sll.append(30)
# # sll.append(40)
# #
# # print("\nList after appending 10,20,30,40:")
# # sll.display()
# #
# # sll.append(50)
# # print("\nList after appending 50:")
# # sll.display()

class Node():
    def __init__(self, toy):
        self.toy = toy
        self.next_car = None # the hook for the next car is empty for now

# This class manages the whole train
class LinkedList:
    def __init__(self):
        self.engine = None # We start with no train cars

    # Let's add a new car to the end of the train
    def add_car(self, toy):
        new_car = Node(toy)

        # If there's no engine yet, this new car is the engine!
        if self.engine is None:
            self.engine = new_car
            return

        # Otherwise, walk to the last car
        last_car = self.engine
        while last_car.next_car:
            last_car = last_car.next_car

        # Hook the new car to the end
        last_car.next_car = new_car

    # Let's see what toys are in our train
    def show_toys(self):
        car = self.engine
        while car:
            print(car.toy, end=" -> ")
            car = car.next_car
        print("End")

# Let's build it!
my_train = LinkedList()
my_train.add_car("Teddy Bear 🧸")
my_train.add_car("Race Car 🏎️")
my_train.add_car("Doll 🎀")

my_train.show_toys()
# Output: Teddy Bear 🧸 -> Race Car 🏎️ -> Doll 🎀 -> End