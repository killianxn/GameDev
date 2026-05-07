# ==============================
# GAME DATA
# ==============================

# Brilyante / Player templates
brilyante_stats = {
    1: {
        "plyr_name": "",
        "name": "Apoy",
        "hp": 30,
        "base_hp": 30,
        "max_hp": 30,
        "atk": 15,
        "def": 10,
        "skill": "Fireball",
        "skill_damage": 30,
        "skill_count": 3,
        "gold": 0,
    },
    2: {
        "plyr_name": "",
        "name": "Tubig",
        "hp": 30,
        "base_hp": 30,
        "max_hp": 30,
        "atk": 14,
        "def": 12,
        "skill": "Tsunami",
        "skill_damage": 28,
        "skill_count": 3,
        "gold": 0,
    },
    3: {
        "plyr_name": "",
        "name": "Hangin",
        "hp": 30,
        "base_hp": 30,
        "max_hp": 30,
        "atk": 13,
        "def": 11,
        "skill": "Tornado",
        "skill_damage": 26,
        "skill_count": 3,
        "gold": 0,
    },
    4: {
        "plyr_name": "",
        "name": "Lupa",
        "hp": 30,
        "base_hp": 30,
        "max_hp": 30,
        "atk": 11,
        "def": 15,
        "skill": "Earthquake",
        "skill_damage": 22,
        "skill_count": 3,
        "gold": 0,
    },
}

# Enemy templates
enemy_stats = {
    1: {"name": "Banak and Nakba", "hp": 25, "atk": 18, "def": 11},
    2: {"name": "Hatorian", "hp": 30, "atk": 20, "def": 13, "l_gold": 20, "w_gold": 120},
    3: {"name": "Agane", "hp": 50, "atk": 30, "def": 18, "l_gold": 20, "w_gold": 170},
    4: {"name": "Hagorn", "hp": 75, "atk": 50, "def": 25, "l_gold": 20, "w_gold": 200},
    5: {"name": "Ether", "hp": 100, "atk": 70, "def": 30, "l_gold": 20, "w_gold": 300},
}

# Shop items
shop_items = {
    1: {"name": "Health Kit", "add": 10, "price": 55, "info": "..."},
    2: {"name": "Attack Kit", "add": 25, "price": 80, "info": "..."},
    3: {"name": "Skill Upgrade", "add": 35, "price": 100, "info": "..."},
    4: {"name": "Defense Upgrade", "add": 25, "price": 80, "info": "..."},
}

# Main menu
menu = ["1. Continue", "2. Exit"]

# Shop menu
option = ["1. Buy", "2. Continue to next level"]


# ==============================
# UTILITY / CORE MECHANICS
# ==============================

def attack_system(attacker_atk, defender_def, defender_hp):
    """Compute damage and apply it to defender_hp."""

    damage = attacker_atk - defender_def
    if damage < 1:
        damage = 1

    new_hp = defender_hp - damage
    return new_hp, damage


def displayMenu():
    """Main menu after tutorial."""
    for menu_item in menu:
        print(menu_item)


def displayOption():
    """Shop options."""
    print("==========================")
    for option_item in option:
        print(option_item)


def displayPlayerStat(player):
    """Print current player stats."""
    print(f"\n===== {player['plyr_name']} Statistics =====")
    print(f"Name: {player['plyr_name']}")
    print(f"Brilyante: {player['name']}")
    print(f"HP: {player['hp']} / {player['max_hp']}")
    print(f"ATK: {player['atk']}")
    print(f"Defense: {player['def']}")
    print(f"Special Skill: {player['skill']}")
    print(f"Skill Damage: {player['skill_damage']}")
    print(f"Skill Count: {player['skill_count']}")
    print(f"Gold: {player['gold']}")


# ==============================
# PLAYER SETUP
# ==============================

def createPlayer():
    """Ask the user for name + brilyante selection and return a player dict."""

    print("\n===========================================")
    name = input("What is your name? ").capitalize()

    while True:
        print("Choose your Brilyante:")
        action = int(
            input(
                "1. Brilyante ng Apoy\n"
                "2. Brilyante ng Tubig\n"
                "3. Brilyante ng Hangin\n"
                "4. Brilyante ng Lupa\n"
                "Enter the number of your choice: "
            )
        )

        if action in brilyante_stats:
            break
        else:
            print("Invalid choice! Please pick a number from 1 to 4.\n")

    player = brilyante_stats[action].copy()
    player["plyr_name"] = name

    # baseline HP before any shop upgrades
    player["base_hp"] = player["hp"]
    player["max_hp"] = player["hp"]

    print(f"\nWelcome, {player['plyr_name']}!")
    print(f"You chose Brilyante ng {player['name']}")

    print(f"\n===== {player['plyr_name']} Statistics =====")
    print(f"HP: {player['hp']} / {player['max_hp']}")
    print(f"ATK: {player['atk']}")
    print(f"Defense: {player['def']}")
    print(f"Special Skill: {player['skill']}")
    print(f"Skill Damage: {player['skill_damage']}")
    print(f"Skill Count: {player['skill_count']}")
    print(f"Gold: {player['gold']}")

    start = input("\nStart your journey? (YES or NO) ").upper()
    if start == "YES":
        return player

    intro()
    return None

def intro():
    """Game intro entry point."""
    print("Welcome to the Encantadia! Traveler!")
    choice = input("Ready for an adventure? (YES or NO) ").upper()

    if choice == "YES":
        player = createPlayer()
        if player is None:
            return
        dungeonTutorial(player)
    else:
        print("You left the game!")


# ==============================
# SHOP SYSTEM
# ==============================

def add_hp(player, amount):
    # Health Kit: increases BOTH current HP and max HP
    player["max_hp"] += amount
    player["hp"] = min(player["max_hp"], player["hp"] + amount)
    print(f"\nHP increased by {amount}!")


def add_attack(player, amount):
    player["atk"] += amount
    print(f"\nAttack increased by {amount}!")


def add_skill(player, amount):
    player["skill_damage"] += amount
    print(f"\nSkill Damage increased by {amount}!")


def add_defense(player, amount):
    player["def"] += amount
    print(f"\nDefense increased by {amount}!")


def buy_item(player, item_choice):
    """Buy shop item and apply its stat changes."""

    if item_choice not in shop_items:
        print("Invalid Item!")
        return

    item = shop_items[item_choice]

    if player["gold"] < item["price"]:
        print("\nNot enough gold!")
        return

    player["gold"] -= item["price"]

    if item_choice == 1:
        add_hp(player, item["add"])
    elif item_choice == 2:
        add_attack(player, item["add"])
    elif item_choice == 3:
        add_skill(player, item["add"])
    elif item_choice == 4:
        add_defense(player, item["add"])

    print(f"\nYou bought {item['name']}!")
    print(f"Remaining Gold: {player['gold']}")


def shop(player):
    """Loop shop until player continues to next level."""

    print(f"\n{player['plyr_name']}'s Gold: {player['gold']}")

    while True:
        print("\n===== IMAW'S SHOP =====")

        for key, value in shop_items.items():
            print(
                f"""
[{key}] {value['name']}
    Effect : +{value['add']}
    Price  : {value['price']} Gold
    Info   : {value['info']}
                """
            )

        displayOption()
        try:
            pickedOption = int(input("Choose Action: "))
        except ValueError:
            print("Invalid Option!")
            continue

        if pickedOption == 1:
            try:
                item_choice = int(input("\nEnter item number to buy: "))
            except ValueError:
                print("Invalid item choice!")
                continue

            buy_item(player, item_choice)
            print("\n===== UPDATED STATS =====")
            displayPlayerStat(player)

        elif pickedOption == 2:
            print("\nProceeding to next level...")
            return
        else:
            print("Invalid Option!")


# ==============================
# BATTLE SYSTEM
# ==============================

def post_level_reward(player):
    """Reward after clearing a level/boss."""

    print("\n===== LEVEL CLEARED =====")

    player["skill_count"] = 3
    print("Skill count restored!")

    player["hp"] = player["max_hp"]

    print(f"HP restored to max HP cap: {player['max_hp']}!")
    print(f"Current HP: {player['hp']}")


def dungeonTutorial(player):
    """Tutorial battle (level 1), then continues to shop + startGame."""

    print("\n===== DUNGEON TUTORIAL =====")
    enemy = enemy_stats[1].copy()

    print(f"\nA wild {enemy['name']} appeared!\n")
    print(f"Your HP: {player['hp']} / {player['max_hp']}")
    print(f"{enemy['name']} HP: {enemy['hp']}\n")

    while player["hp"] > 0 and enemy["hp"] > 0:
        print("Tutorial: Pick a number to start your turn.")
        print("\n===== YOUR TURN =====")
        print("1. Basic Attack")
        print("2. Special Skill")
        print("3. Exit battle")

        move = input("Choose attack: ")

        if move == "3":
            print("\nYou exited the battle!\n")
            return

        if move == "1":
            enemy["hp"], damage = attack_system(player["atk"], enemy["def"], enemy["hp"])
            enemy["hp"] = max(0, enemy["hp"])
            print(f"\nYou dealt {damage} damage!")
            print(f"{enemy['name']} health is now {enemy['hp']}")

        elif move == "2":
            enemy["hp"], damage = attack_system(player["skill_damage"], enemy["def"], enemy["hp"])
            enemy["hp"] = max(0, enemy["hp"])
            player["skill_count"] -= 1
            print(f"\nYou dealt {damage} damage!")
            print(f"Enemy health is now {enemy['hp']}")
            print(f"Special Skill remaining: {player['skill_count']}")
        else:
            print("Invalid move!")
            continue

        if enemy["hp"] == 0:
            print(f"\n{enemy['name']} was defeated!")
            post_level_reward(player)
            break

        # ENEMY TURN
        print(f"\n===== {enemy['name'].upper()} TURN =====")
        player["hp"], enemy_damage = attack_system(enemy["atk"], player["def"], player["hp"])
        player["hp"] = max(0, player["hp"])

        print(f"\n{enemy['name']} attacked!")
        print(f"{enemy['name']} dealt {enemy_damage} damage!")
        print(f"Your health is now {player['hp']}")
        print(f"\nYour HP: {player['hp']} / {player['max_hp']}")
        print(f"{enemy['name']} HP: {enemy['hp']}\n")

    if player["hp"] <= 0:
        print("\nGAME OVER!")
        return

    print("\nCongratulations!")
    print("You cleared the tutorial!")
    print("You earned 150 Gold\n\n")
    player["gold"] += 150

    displayPlayerStat(player)

    print("\nOnce you defeat a level, you may proceed to Shop")
    displayMenu()
    choice = int(input("Choose Action: "))

    if choice == 1:
        shop(player)
        startGame(player)
    elif choice == 2:
        exit()
    else:
        print("Invalid Input!")


def startGame(player):
    """Main game loop: fights enemies 2 to 5."""

    for enemy_id in range(2, 6):
        enemy = enemy_stats[enemy_id].copy()

        print("\n===================================")
        print(f"\nA wild {enemy['name']} appeared!")

        while player["hp"] > 0 and enemy["hp"] > 0:
            print(f"\n===== {player['plyr_name'].upper()} TURN =====")
            print(f"Your HP: {player['hp']} / {player['max_hp']}")
            print(f"{enemy['name']} HP: {enemy['hp']}")

            print("\n1. Basic Attack")
            print("2. Special Skill")
            print("3. Exit battle")

            move = input("Choose attack: ")

            if move == "3":
                print("\nYou exited the battle!\n")
                return

            if move == "1":
                enemy["hp"], damage = attack_system(player["atk"], enemy["def"], enemy["hp"])
                enemy["hp"] = max(0, enemy["hp"])
                print(f"\nYou dealt {damage} damage!")
                print(f"{enemy['name']} HP is now {enemy['hp']}")

            elif move == "2":
                if player["skill_count"] <= 0:
                    print("\nNo skills remaining!")
                    continue

                enemy["hp"], damage = attack_system(player["skill_damage"], enemy["def"], enemy["hp"])
                enemy["hp"] = max(0, enemy["hp"])
                player["skill_count"] -= 1

                print(f"\nYou used {player['skill']}!")
                print(f"You dealt {damage} damage!")
                print(f"{enemy['name']} HP is now {enemy['hp']}")
                print(f"Skill uses left: {player['skill_count']}")
            else:
                print("\nInvalid move!")
                continue

            if enemy["hp"] == 0:
                print(f"\n{enemy['name']} was defeated!")
                player["gold"] += enemy["w_gold"]
                print(f"You earned {enemy['w_gold']} Gold!")

                post_level_reward(player)
                displayPlayerStat(player)

                shop(player)
                break

            # ENEMY TURN
            print(f"\n===== {enemy['name'].upper()} TURN =====")
            player["hp"], enemy_damage = attack_system(enemy["atk"], player["def"], player["hp"])
            player["hp"] = max(0, player["hp"])

            print(f"\n{enemy['name']} attacked!")
            print(f"{enemy['name']} dealt {enemy_damage} damage!")
            print(f"Your HP is now {player['hp']} / {player['max_hp']}")

        if player["hp"] <= 0:
            print("\nGAME OVER!")
            return

    print("\n===================================")
    print("CONGRATULATIONS!")
    print("You defeated all enemies!")


# ==============================
# START GAME
# ==============================

intro()
