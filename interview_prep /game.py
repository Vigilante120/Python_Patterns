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


print("Welcome to the Shadows. Your Mission Begins Now")

while True:
    action = input("\nWhat will you do? (loot / drop / heal / inspect / attack / quit): ").lower()

    if action == "quit" or action == "q":
        print("Disappearing in the shadows. Bye")
        break
    
    elif action == "loot":
        item = input("What item do you want to loot? [hidden blade, smoke, kunai]").lower()
        loot_item(item)
    
    elif action == "drop":
        drop = input("What item you want to drop ? ").lower()
        drop_item(drop)
    
    elif action == "attack":
        enemy = input("Which enemy will you attack? ").lower()
        attack(enemy)
    
    elif action == "heal":
        try:
            heal_item = int(input("how much do you want to heal: "))
            heal(heal_item)
        except:
            ValueError("Please enter the Value in Numbers [1,2,3,4..0]")
        

    elif action == "inspect":
        enemy = input("Which enemy you want to inspect? ").lower()
        inspect_enemy(enemy)
    
    else:
        print("Invalid Action. Please Choose from the list")