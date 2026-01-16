# here we will practice .keys()
"""
Docstring for graphs.keys_explaination

this is .keys() it returns a collection view or view object. 
"""

user_score = {"nishant": 95,
              "som": 90,
              "yapper": 89
              }

all_names = user_score.keys()
print(all_names)

# output: 
# dict_keys(['nishant', 'som', 'yapper'])

# only the keys are extracted thats it 

"""
3 golden rules not to forget the .keys function 
1. It creates a "Window," not a "Copy"
This is the part that trips people up. In Python, all_names isn't a static list; it's a view.

If you change the dictionary, the all_names variable updates automatically without you having to call .keys() again.

"""

user_score = {"nishant": 95, "som": 90}
all_names = user_score.keys()

# Add someone new
user_score["rohit"] = 64

print(all_names) 
# Output: dict_keys(['nishant', 'som', 'new_person']) 
# See? It updated on its own!

"""
2. It’s for "Membership Testing"
The most common reason developers use .keys() is to check if a specific "label" exists before they try to access it (to avoid errors).

Logic: "Do I have a key named 'yapper'?"

Code: if "yapper" in user_score.keys():
"""

if "som" in user_score.keys():
    print(True)
else:
    print(False)

"""
3. You can't use it like a List (yet)

Even though it looks like a list, you can't do things like all_names[0]. It will throw an error.

Think of it this way: A "View" is like looking through a window at a garden. You can see the flowers, but you can't rearrange them until you physically go outside (convert it to a list).

To turn it into a real list: names_list = list(user_score.keys())
"""

