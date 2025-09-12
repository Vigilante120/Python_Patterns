

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # printing the list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("End")

    def append(self, value):
        new_node = Node(value)
        # if empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        # check if the length is 0
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # if not we will assign the head to the new node :)
        # how ? by saying new_node.next = self.head
        # then assign the self.head to new_node.
        else:
            new_node.next = self.head
            self.head = new_node
        # increase the length also.
        self.length += 1
        return True

    def pop_first(self):
        # no items in the LL
        if self.length == 0:
            return None
        # will use temp var to remove the head
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # there is also same condition which was above
        # but this is only after we have decreased the value by 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # as u can see i have put _ instead of i or any other variable
        # its becuz we only use variable when we are going to call it
        # in my case im not going to call it
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        # doing -1 because we need to be at the head
        # then we point to the new value
        temp = self.get(index - 1)
        # pointing to the new node
        new_node.next = temp.next
        # pointing to the node where the head was pointing first
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



# Checking Methods
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.prepend(10)
# my_linked_list.pop_first()
my_linked_list.set_value(1, 11)
my_linked_list.insert(2, 12)
my_linked_list.pop()
my_linked_list.reverse()
my_linked_list.print_list()

