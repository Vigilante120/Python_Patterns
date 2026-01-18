# --- THE ULTIMATE HASH TABLE (DICTIONARY) CHEAT SHEET ---

# 1. INITIALIZATION
my_dict = {"a": 1, "b": 2}          # Standard dict
empty_dict = {}                     # Empty dict
from collections import defaultdict, Counter
d_dict = defaultdict(list)          # Automatically creates [] for new keys
counts = Counter("banana")          # {'b': 1, 'a': 3, 'n': 2}


# 2. ADDING & UPDATING (O(1))
my_dict["c"] = 3                    # Basic insert
my_dict.update({"d": 4, "e": 5})    # Batch insert multiple items


# 3. ACCESSING & CHECKING (O(1))
val = my_dict["a"]                  # Returns 1 (Crashes if key not found)
val = my_dict.get("z", 0)           # Returns 0 if "z" is missing (Safe Access)

if "a" in my_dict:                  # Check if key exists
    print("Found 'a'!")


# 4. VIEWING COMPONENTS
all_keys = my_dict.keys()           # dict_keys(['a', 'b', 'c', ...])
all_vals = my_dict.values()         # dict_values([1, 2, 3, ...])
all_pairs = my_dict.items()         # dict_items([('a', 1), ('b', 2)])

# Useful for looping:
# for k, v in my_dict.items():
#     print(f"Key: {k}, Value: {v}")


# 5. REMOVING (O(1))
removed_val = my_dict.pop("a")      # Removes "a" and returns 1
del my_dict["b"]                    # Deletes "b" (Returns nothing)
last_added = my_dict.popitem()      # Removes and returns last pair (key, val)
my_dict.clear()                     # Wipes the entire dictionary


# 6. HANDY TRICKS FOR INTERVIEWS
# Sorting a dict by values (returns list of tuples)
sorted_by_val = sorted(counts.items(), key=lambda item: item[1], reverse=True)

# Copying
new_copy = my_dict.copy()           # Shallow copy

# Dictionary Comprehension (Creating a dict in 1 line)
squares = {x: x**2 for x in range(5)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# --- COMPLEXITY SUMMARY ---
# Operation | Average Time | Space
# ---------|--------------|-------
# Insert   | O(1)         | O(n)
# Lookup   | O(1)         | -
# Delete   | O(1)         | -

# Frequency map 

votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob"]

count = {}
for name in votes:
    count[name] = count.get(name, 0) + 1

print(count)
