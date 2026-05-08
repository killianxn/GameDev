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

main_menu = (  # Main menu options
    "1. Continue",
    "2. Exit"
)

shop_menu = (  # Shop menu options
    "1. Buy",
    "2. Continue to next level"
)

battle_menu = (  # Battle menu options
    "1. Basic Attack",
    "2. Special Skill",
    "3. Exit Battle"
)


# ==============================
# UTILITY FUNCTIONS
# ==============================

def display_menu(menu):  # Function for displaying menus
    for item in menu:  # Loop through each menu item
        print(item)  # Print menu item


def attack_system(attacker_atk, defender_def, defender_hp):  # Function for calculating damage
    damage = attacker_atk - defender_def   # Calculate damage (attack - defense = total damage)

    if damage < 1:  # Prevent damage lower than 1
        damage = 1   # Minimum damage becomes 1

    defender_hp -= damage   # Reduce defender HP

    return defender_hp, damage  # Return updated HP and damage dealt


def deal_damage(attacker_power, defender_def, target):  # Function that applies damage to target
    target["hp"], damage = attack_system(  # Call attack_system function
        attacker_power,  # Attacker power argument
        defender_def,  # Defender defense argument
        target["hp"]  # Target HP argument
    )

    target["hp"] = max(0, target["hp"])  # max(0 <max>, target['hp'] <comaprison>) if hp negative, will return 0 <returns which value higher>
    return damage  # Return damage value


def displayPlayerStat(player):  # Function that displays player stats
    print(f"\n===== {player['plyr_name']} Statistics =====")  # Print stat title
    print(f"Brilyante: {player['name']}")   # Print Brilyante type
    print(f"HP: {player['hp']} / {player['max_hp']}")  # Print HP
    print(f"ATK: {player['atk']}")  # Print attack stat
    print(f"Defense: {player['def']}")  # Print defense stat
    print(f"Special Skill: {player['skill']}")  # Print skill name
    print(f"Skill Damage: {player['skill_damage']}")  # Print skill damage
    print(f"Skill Count: {player['skill_count']}")  # Print remaining skill count
    print(f"Gold: {player['gold']}")  # Print gold amount


def post_level_reward(player):  # Function for restoring player after level
    print("\n===== LEVEL CLEARED =====")   # Print level clear message

    player["skill_count"] = 3   # Restore skill count
    player["hp"] = player["max_hp"]   # Fully heal player

    print("Skill count restored!")  # Notify player
    print(f"HP restored to {player['max_hp']}!")  # Display restored HP


# ==============================
# PLAYER SETUP
# ==============================

def createPlayer():  # Function for creating player
    print("\n===================================") # Display separator

    name = input("What is your name? ").capitalize() # Ask player name with capitalized first letter

    print("\nChoose your Brilyante:")  # Display Brilyante choices

    while True:  # Infinite loop until valid choice

        try:
            choice = int(input(   # Ask for player choice
                "1. Brilyante ng Apoy\n"
                "2. Brilyante ng Tubig\n"
                "3. Brilyante ng Hangin\n"
                "4. Brilyante ng Lupa\n"
                "Enter choice: "
            ))

            if choice in brilyante_stats:   # Check if choice exists
                break   # Exit loop if valid

            print("Invalid choice!")   # Invalid choice message

        except ValueError:   # Error if input is not number
            print("Enter numbers only!")  # error message

    player = brilyante_stats[choice].copy()  # Copy chosen Brilyante stats

    player["plyr_name"] = name   # Save player name

    print(f"\nWelcome, {name}!")   # Welcome message
    print(f"You chose Brilyante ng {player['name']}")  # Show chosen Brilyante

    displayPlayerStat(player)  # calling display stat function, argument is for chosen brilyante

    return player # Return player dictionary


def intro(): # Function for game introduction
    print("Welcome to Encantadia!")  # Welcome message

    start = input("Ready for adventure? (YES or NO): ").upper()  # Ask player, makes answer all uppercase letters

    if start == "YES":  # Check if player wants to continue

        player = createPlayer()  # calls createPlayer function and stores returned variable to player

        print("\n===== TUTORIAL =====")  # Tutorial title
        print("Defeat enemies to earn gold.")  # Tutorial instruction
        print("Use skills wisely.")  # Tutorial instruction
        print("After every battle, you may visit the shop.\n")   # Tutorial instruction

        startGame(player)  # calls startGame with player argument (values stored inside the variable will be used inside the startGame function)

    else:  # If player answered NO
        print("You left the game!")  # Exit message


# ==============================
# SHOP SYSTEM
# ==============================

def upgrade_stat(player, stat, amount):  # Function for upgrading player stats
    if stat == "max_hp":  # Check if upgrading max HP

        player["max_hp"] += amount  # Increase max HP

        player["hp"] = min(   # Heal player without exceeding max HP
            player["max_hp"],  # Maximum possible HP
            player["hp"] + amount  # Current HP plus added amount
        )

    else:
        player[stat] += amount   # Increase selected stat

    print(f"{stat.upper()} increased by {amount}!")  # Upgrade message


def buy_item(player, item_choice):  # Function for buying shop items
    if item_choice not in shop_items:  # Check if item exists
        print("Invalid Item!")  # Error message
        return   # Stop function

    item = shop_items[item_choice]  # Store selected item

    if player["gold"] < item["price"]:   # Check if player has enough gold
        print("\nNot enough gold!")   # Not enough gold message
        return  # Stop function

    player["gold"] -= item["price"]  # Deduct gold from player

    upgrade_stat(  # calls upgrade_stat function with arguments to access value
        player,
        item["stat"],
        item["add"]
    )

    print(f"\nYou bought {item['name']}!")  # Purchase confirmation
    print(f"Remaining Gold: {player['gold']}")  # Display remaining gold


def shop(player):  # Function for shop system
    while True:  # Infinite shop loop

        print("\n===== IMAW'S SHOP =====")  # Shop title
        print(f"Gold: {player['gold']}")   # Display current gold

        for key, value in shop_items.items():   # Loop through shop items

            print(f"""
[{key}] {value['name']}
Effect : +{value['add']}
Price  : {value['price']} Gold
Info   : {value['info']}
            """)  # formatted displaying item information

        display_menu(shop_menu)   # Display shop menu options

        try:  # Handle invalid input
            option = int(input("Choose Action: "))  # Ask player action

        except ValueError:   # If input is not a number
            print("Invalid input!")  # Error message
            continue  # Restart loop

        if option == 1:  # Buy item option

            try:  # Handle invalid item input
                item_choice = int(input("Enter item number: "))  # Ask item number
                buy_item(player, item_choice)  # calls function buy_item with argu to store player values and item chosen

                print("\n===== UPDATED STATS =====")  # Updated stats title
                displayPlayerStat(player)  # Display updated player stats

            except ValueError:  # If invalid input
                print("Invalid item!")  # Error message

        elif option == 2:  # Continue option
            print("\nProceeding to next level...")  # Continue message
            return  # Exit shop

        else:  # Invalid menu option
            print("Invalid Option!")  # Error message


# ==============================
# BATTLE SYSTEM
# ==============================

def player_turn(player, enemy):  # Function for player's turn in battle
    print(f"\n===== {player['plyr_name'].upper()} TURN =====") # Show player turn header

    print(f"Your HP: {player['hp']} / {player['max_hp']}")   # Show player HP status
    print(f"{enemy['name']} HP: {enemy['hp']}")  # Show enemy HP status

    display_menu(battle_menu)  # function call to display ung choices

    move = input("Choose attack: ")  # Ask player for move

    # BASIC ATTACK
    if move == "1":  # Basic attack option

        damage = deal_damage(  # calls function for dealing damage
            player["atk"],  # arguments
            enemy["def"],  #arguments
            enemy  # arguments
        )

        print(f"\nYou dealt {damage} damage!")  # Show damage dealt
        print(f"{enemy['name']} HP is now {enemy['hp']}")  # Show updated enemy HP

    # SKILL ATTACK
    elif move == "2":  # Skill attack option

        if player["skill_count"] <= 0:  # Check skill availability
            print("\nNo skills remaining!")   # No skill message
            return True# Continue battle

        damage = deal_damage(   # Apply skill damage
            player["skill_damage"],  # Skill power argu
            enemy["def"],  # Enemy defense argu
            enemy  # Enemy target argu
        )

        player["skill_count"] -= 1  # Reduce skill uses

        print(f"\nYou used {player['skill']}!")   # Skill name message
        print(f"You dealt {damage} damage!")   # Damage message
        print(f"Skill uses left: {player['skill_count']}")  # Remaining skill uses

    # EXIT
    elif move == "3":   # Exit battle option
        print("\nYou exited the battle!")  # Exit message
        return False   # Stop battle

    else:   # Invalid input
        print("Invalid move!")  # Error message

    return True  # Continue battle


def enemy_turn(player, enemy):   # Function for enemy attack turn
    print(f"\n===== {enemy['name'].upper()} TURN =====")  # Enemy turn header

    damage = deal_damage( # Apply skill damage
        enemy["atk"],  # Skill power argu
        player["def"],  # player defense argu
        player  #player target argu
    )

    print(f"{enemy['name']} attacked!")  #attack notifier
    print(f"{enemy['name']} dealt {damage} damage!")  # Damage message

    print(f"Your HP is now {player['hp']} / {player['max_hp']}")  # Updated HP display


def startGame(player):  # Main game loop function
    for enemy_id in enemy_stats:   # Loop through every enemy

        enemy = enemy_stats[enemy_id].copy()   # Copy enemy stats (enemy_id = ung 1 - 6)

        print("\n===================================") # Display separator
        print(f"\nA wild {enemy['name']} appeared!")  # Enemy encounter message

        # Tutorial message only for first enemy
        if enemy_id == 1:  # Check if tutorial enemy
            print("\n[Tutorial Enemy]")   # Tutorial label
            print("Choose attacks using numbers.")  # Tutorial instruction

        while player["hp"] > 0 and enemy["hp"] > 0:  # Battle loop, wont end until not defeated

            continue_battle = player_turn(player, enemy) # placed function inside a variable for dynamic use

            if continue_battle is False:  # Check if player exited
                return   # Stop the game

            # Enemy defeated
            if enemy["hp"] <= 0:  # Check if enemy died

                print(f"\n{enemy['name']} was defeated!") # Defeat message

                # gold reward
                player["gold"] += enemy["gold"] # Give gold reward

                print(f"You earned {enemy['gold']} Gold!")  # Show gold reward

                # skill damage buff
                player["skill_damage"] += 8

                print("Your special skill became stronger!")  # Buff message
                print(f"Skill Damage increased by 8!")   # Buff amount
                print(f"Current Skill Damage: {player['skill_damage']}")  # Display updated skill damage

                post_level_reward(player)   # call function for player restoration

                displayPlayerStat(player)  # call function to display updated stats

                # Last enemy
                if enemy_id == 5:  # Check if final enemy was defeated 
                    print("\n===================================")   # Display separator
                    print("CONGRATULATIONS!")   # Victory message
                    print("You defeated all enemies!")  # End game message
                    return   # End game

                display_menu(main_menu)  # if not enemy 5, skips that condition, proceeds here

                try:  # Handle invalid input
                    choice = int(input("Choose Action: "))  # Ask player choice
 
                    if choice == 1:  # Continue option
                        shop(player)   # Open shop

                    elif choice == 2:  # Exit option
                        print("Thanks for playing!")  # Exit message
                        return   # End game

                except ValueError:  # If input is invalid
                    print("Invalid input!")  # Error message

                break   # Exit battle loop after victory

            # Enemy attacks
            enemy_turn(player, enemy)  # function for enemy turn

            # Game over
            if player["hp"] <= 0:  # Check if player died

                print(f"\nYou were defeated by {enemy['name']}!")  # Defeat message

                # Restore player
                player["hp"] = player["max_hp"]  # hp restore
                player["skill_count"] = 3  # skill restore

                # TUTORIAL ENEMY
                if enemy_id == 1:  # Tutorial enemy check

                    print("\nRetrying tutorial battle...")  # Retry message

                    # restart same tutorial enemy
                    enemy = enemy_stats[enemy_id].copy()   # Reset tutorial enemy

                # NORMAL ENEMIES
                else:

                    # consolation gold
                    player["gold"] += 20

                    print("You received 20 Gold.")  # Gold message
                    print(f"Current Gold: {player['gold']}")  # Display updated gold

                    print("\nYou were brought back to the shop.")  # Shop message

                    # open shop
                    shop(player)  # calls shop function

                    # retry same enemy
                    enemy = enemy_stats[enemy_id].copy()

                    print(f"\nYou are challenging {enemy['name']} again!") # Retry battle message


# ==============================
# START GAME
# ==============================

intro()
