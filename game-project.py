# ==============================
# GAME DATA
# ==============================

# Brilyante / Player templates
brilyante_stats = {
    1: {
        "plyr_name": "",
        "name": "Apoy",
        "hp": 30,
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
    1: {"name": "Banak and Nakba", "hp": 25, "atk": 18, "def": 11, "gold": 150},
    2: {"name": "Hatorian", "hp": 30, "atk": 20, "def": 13, "gold": 120},
    3: {"name": "Agane", "hp": 50, "atk": 30, "def": 18, "gold": 170},
    4: {"name": "Hagorn", "hp": 75, "atk": 50, "def": 25, "gold": 200},
    5: {"name": "Ether", "hp": 100, "atk": 70, "def": 30, "gold": 300},
}


# Shop items
shop_items = {
    1: {
        "name": "Health Kit",
        "stat": "max_hp",
        "add": 10,
        "price": 55,
        "info": "Increase HP"
    },

    2: {
        "name": "Attack Kit",
        "stat": "atk",
        "add": 25,
        "price": 80,
        "info": "Increase Attack"
    },

    3: {
        "name": "Skill Upgrade",
        "stat": "skill_damage",
        "add": 35,
        "price": 100,
        "info": "Increase Skill Damage"
    },

    4: {
        "name": "Defense Upgrade",
        "stat": "def",
        "add": 25,
        "price": 80,
        "info": "Increase Defense"
    },
}


# ==============================
# MENUS (TUPLES)
# ==============================

main_menu = (
    "1. Continue",
    "2. Exit"
)

shop_menu = (
    "1. Buy",
    "2. Continue to next level"
)

battle_menu = (
    "1. Basic Attack",
    "2. Special Skill",
    "3. Exit Battle"
)


# ==============================
# UTILITY FUNCTIONS
# ==============================

def display_menu(menu):
    """Display menu options."""
    for item in menu:
        print(item)


def attack_system(attacker_atk, defender_def, defender_hp):
    """Compute damage."""

    damage = attacker_atk - defender_def

    if damage < 1:
        damage = 1

    defender_hp -= damage

    return defender_hp, damage


def deal_damage(attacker_power, defender_def, target):
    """Apply damage to target."""

    target["hp"], damage = attack_system(
        attacker_power,
        defender_def,
        target["hp"]
    )

    target["hp"] = max(0, target["hp"])

    return damage


def displayPlayerStat(player):
    """Display player statistics."""

    print(f"\n===== {player['plyr_name']} Statistics =====")
    print(f"Brilyante: {player['name']}")
    print(f"HP: {player['hp']} / {player['max_hp']}")
    print(f"ATK: {player['atk']}")
    print(f"Defense: {player['def']}")
    print(f"Special Skill: {player['skill']}")
    print(f"Skill Damage: {player['skill_damage']}")
    print(f"Skill Count: {player['skill_count']}")
    print(f"Gold: {player['gold']}")


def post_level_reward(player):
    """Restore player after winning."""

    print("\n===== LEVEL CLEARED =====")

    player["skill_count"] = 3
    player["hp"] = player["max_hp"]

    print("Skill count restored!")
    print(f"HP restored to {player['max_hp']}!")


# ==============================
# PLAYER SETUP
# ==============================

def createPlayer():
    """Create player."""

    print("\n===================================")

    name = input("What is your name? ").capitalize()

    print("\nChoose your Brilyante:")

    while True:

        try:
            choice = int(input(
                "1. Brilyante ng Apoy\n"
                "2. Brilyante ng Tubig\n"
                "3. Brilyante ng Hangin\n"
                "4. Brilyante ng Lupa\n"
                "Enter choice: "
            ))

            if choice in brilyante_stats:
                break

            print("Invalid choice!")

        except ValueError:
            print("Enter numbers only!")

    player = brilyante_stats[choice].copy()

    player["plyr_name"] = name

    print(f"\nWelcome, {name}!")
    print(f"You chose Brilyante ng {player['name']}")

    displayPlayerStat(player)

    return player


def intro():
    """Game intro."""

    print("Welcome to Encantadia!")

    start = input("Ready for adventure? (YES or NO): ").upper()

    if start == "YES":

        player = createPlayer()

        print("\n===== TUTORIAL =====")
        print("Defeat enemies to earn gold.")
        print("Use skills wisely.")
        print("After every battle, you may visit the shop.\n")

        startGame(player)

    else:
        print("You left the game!")


# ==============================
# SHOP SYSTEM
# ==============================

def upgrade_stat(player, stat, amount):
    """Upgrade player stats."""

    if stat == "max_hp":

        player["max_hp"] += amount

        player["hp"] = min(
            player["max_hp"],
            player["hp"] + amount
        )

    else:
        player[stat] += amount

    print(f"{stat.upper()} increased by {amount}!")


def buy_item(player, item_choice):
    """Buy shop item."""

    if item_choice not in shop_items:
        print("Invalid Item!")
        return

    item = shop_items[item_choice]

    if player["gold"] < item["price"]:
        print("\nNot enough gold!")
        return

    player["gold"] -= item["price"]

    upgrade_stat(
        player,
        item["stat"],
        item["add"]
    )

    print(f"\nYou bought {item['name']}!")
    print(f"Remaining Gold: {player['gold']}")


def shop(player):
    """Shop loop."""

    while True:

        print("\n===== IMAW'S SHOP =====")
        print(f"Gold: {player['gold']}")

        for key, value in shop_items.items():

            print(f"""
[{key}] {value['name']}
Effect : +{value['add']}
Price  : {value['price']} Gold
Info   : {value['info']}
            """)

        display_menu(shop_menu)

        try:
            option = int(input("Choose Action: "))

        except ValueError:
            print("Invalid input!")
            continue

        if option == 1:

            try:
                item_choice = int(input("Enter item number: "))
                buy_item(player, item_choice)

                print("\n===== UPDATED STATS =====")
                displayPlayerStat(player)

            except ValueError:
                print("Invalid item!")

        elif option == 2:
            print("\nProceeding to next level...")
            return

        else:
            print("Invalid Option!")


# ==============================
# BATTLE SYSTEM
# ==============================

def player_turn(player, enemy):
    """Handle player attack turn."""

    print(f"\n===== {player['plyr_name'].upper()} TURN =====")

    print(f"Your HP: {player['hp']} / {player['max_hp']}")
    print(f"{enemy['name']} HP: {enemy['hp']}")

    display_menu(battle_menu)

    move = input("Choose attack: ")

    # BASIC ATTACK
    if move == "1":

        damage = deal_damage(
            player["atk"],
            enemy["def"],
            enemy
        )

        print(f"\nYou dealt {damage} damage!")
        print(f"{enemy['name']} HP is now {enemy['hp']}")

    # SKILL ATTACK
    elif move == "2":

        if player["skill_count"] <= 0:
            print("\nNo skills remaining!")
            return True

        damage = deal_damage(
            player["skill_damage"],
            enemy["def"],
            enemy
        )

        player["skill_count"] -= 1

        print(f"\nYou used {player['skill']}!")
        print(f"You dealt {damage} damage!")
        print(f"Skill uses left: {player['skill_count']}")

    # EXIT
    elif move == "3":
        print("\nYou exited the battle!")
        return False

    else:
        print("Invalid move!")

    return True


def enemy_turn(player, enemy):
    """Handle enemy attack."""

    print(f"\n===== {enemy['name'].upper()} TURN =====")

    damage = deal_damage(
        enemy["atk"],
        player["def"],
        player
    )

    print(f"{enemy['name']} attacked!")
    print(f"{enemy['name']} dealt {damage} damage!")

    print(f"Your HP is now {player['hp']} / {player['max_hp']}")


def startGame(player):
    """Main game loop."""

    for enemy_id in enemy_stats:

        enemy = enemy_stats[enemy_id].copy()

        print("\n===================================")
        print(f"\nA wild {enemy['name']} appeared!")

        # Tutorial message only for first enemy
        if enemy_id == 1:
            print("\n[Tutorial Enemy]")
            print("Choose attacks using numbers.")

        while player["hp"] > 0 and enemy["hp"] > 0:

            continue_battle = player_turn(player, enemy)

            if continue_battle is False:
                return

            # Enemy defeated
            if enemy["hp"] <= 0:

                print(f"\n{enemy['name']} was defeated!")

                # gold reward
                player["gold"] += enemy["gold"]

                print(f"You earned {enemy['gold']} Gold!")

                # skill damage buff
                player["skill_damage"] += 8

                print("Your special skill became stronger!")
                print(f"Skill Damage increased by 8!")
                print(f"Current Skill Damage: {player['skill_damage']}")

                post_level_reward(player)

                displayPlayerStat(player)

                # Last enemy
                if enemy_id == 5:
                    print("\n===================================")
                    print("CONGRATULATIONS!")
                    print("You defeated all enemies!")
                    return

                display_menu(main_menu)

                try:
                    choice = int(input("Choose Action: "))

                    if choice == 1:
                        shop(player)

                    elif choice == 2:
                        print("Thanks for playing!")
                        return

                except ValueError:
                    print("Invalid input!")

                break

            # Enemy attacks
            enemy_turn(player, enemy)

            # Game over
            # if player["hp"] <= 0:
            #     print("\nYou were defeated!")

            # # consolation gold
            # player["gold"] += 20

            # print("You received 20 Gold.")
            # print(f"Current Gold: {player['gold']}")

            # # restore player
            # player["hp"] = player["max_hp"]
            # player["skill_count"] = 3

            # print("\nYou were brought back to the shop.")

            # # go back to shop
            # shop(player)

            # # retry same enemy
            # enemy = enemy_stats[enemy_id].copy()

            # print(f"\nYou are challenging {enemy['name']} again!")

            # Game over
            if player["hp"] <= 0:

                print(f"\nYou were defeated by {enemy['name']}!")

                # Restore player
                player["hp"] = player["max_hp"]
                player["skill_count"] = 3

                # TUTORIAL ENEMY
                if enemy_id == 1:

                    print("\nRetrying tutorial battle...")

                    # restart same tutorial enemy
                    enemy = enemy_stats[enemy_id].copy()

                # NORMAL ENEMIES
                else:

                    # consolation gold
                    player["gold"] += 20

                    print("You received 20 Gold.")
                    print(f"Current Gold: {player['gold']}")

                    print("\nYou were brought back to the shop.")

                    # open shop
                    shop(player)

                    # retry same enemy
                    enemy = enemy_stats[enemy_id].copy()

                    print(f"\nYou are challenging {enemy['name']} again!")


# ==============================
# START GAME
# ==============================

intro()
