# dictionary Key:value Pair 
# set_item(key, value)

# hash will be added to nails, nuts, screws
# collision happens when 2 vals are entered inside the same address

# find empty spot then store the data inside this that is called linear probing (open addressing) where u dont have more than 1 key:val pair at any address #0x

# seperate chaining is storing all the address like having linked list and say we have multiple vals we iterate through it to find the value we need this is the way to deal with collisons !!!this is imp to understand hashtables

# always have a prime numbers of address 0 - 7

class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size # create a list of 7 items in it 

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


# Time to create a get function here so we can access the values using keys :) 

    def get_item(self, key): # we hit the key and get the value
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            # 2nd loop to get the keys :) 
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

# EXAMPLE USAGE
my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))

print(my_hash_table.keys())
