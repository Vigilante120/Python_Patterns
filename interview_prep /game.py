# now im creating a game to stronghold the basics - text based rpg 

# a hidden blade , smoke bomb and kunai 

player_stats = {
    "health": 50,
    "stamina": 50,
    "level": 1
}

bestiary = {
    "goblin": {"health": 30, "weakness": "hidden blade"},
    "brute": {"health": 80, "weakness": "smoke bomb"},
    "giant": {"health": 50, "weakness": "kunai"}
}

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

def heal(amount):
    player_stats["health"] += amount
    if player_stats["health"] > 100:
        player_stats["health"] = 100
    print(f"You healed! Current Health: {player_stats['health']}")


def inspect_enemy(enemy_name):
    clean_name = enemy_name.lower()
    enemy_data = bestiary.get(clean_name)

    if enemy_data is None:
        print(f"{enemy_name} Not Found.")
    else:
        print(f"---ENEMY: {clean_name.capitalize()}---")
        print(f"Health: {enemy_data['health']}")
        print(f"Weakness: {enemy_data['weakness']}")


# building the combat system

def attack(enemy_name):
    clean_name = enemy_name.lower()
    enemy_data = bestiary.get(clean_name)

    if enemy_data is None:
        print(f"[-]Error {clean_name.capitalize()} is not in the bestiary.")
    else:
        weakness = enemy_data['weakness']
        print(f"Enemy Weakness: {weakness}")

        if weakness in inventory:
            print(f"SUCCESS! You exploited the {clean_name.capitalize()}'s weakness with the {weakness}!")
        else:
            print(f"FAILURE! You don't have the right weapon! You need a {weakness}.")

item = input("Enter the item name: ")
loot_item(item)

print("Current Inventory: ", inventory)

item = input("Enter the item name you want to drop: ")
drop_item(item)

print("Current item in inventory: ", inventory)

heal(30)

enemy_attack = input("Enter the name of enemy: ")

attack(enemy_attack)
