# now im creating a game to stronghold the basics - text based rpg 

# a hidden blade , smoke bomb and kunai 

valid_items = ["hidden blade", "kunai", "smoke bomb"]
inventory = []

def loot_item(item_name):
    clean_name = item_name.lower()
    if clean_name in valid_items:
        inventory.append(clean_name)
        print(f"You picked up a {clean_name}")
    else:
        print(f"There is no {clean_name} here to pick up")

def drop_item(item_name):
    clean_name = item_name.lower()
    if clean_name in inventory:
        inventory.remove(clean_name)
        print(f"you dropped a {clean_name}")
    else:
        print(f"there is no {item_name}")

item = input("Enter the item name: ")
loot_item(item)

print("Current Inventory: ", inventory)

item = input("Enter the item name you want to drop: ")
drop_item(item)

print("Dropped item: ", item)