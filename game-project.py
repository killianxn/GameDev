#disctionaries
brilyante_stats = {
    1: {
        "plyr_name": "",
        "name": "Apoy",
        "hp": 30,
        "atk": 15,
        "def": 10,
        "skill": "Fireball",
        "skill_damage": 30,
        "skill_count": 3,
        "gold": 0
    },

    2: {
        "plyr_name": "",
        "name": "Tubig",
        "hp": 30,
        "atk": 14,
        "def": 12,
        "skill": "Tsunami",
        "skill_damage": 28,
        "skill_count": 3,
        "gold": 0
    },

    3: {
        "plyr_name": "",
        "name": "Hangin",
        "hp": 30,
        "atk": 13,
        "def": 11,
        "skill": "Tornado",
        "skill_damage": 26,
        "skill_count": 3,
        "gold": 0
    },

    4: {
        "plyr_name": "",
        "name": "Lupa",
        "hp": 30,
        "atk": 11,
        "def": 15,
        "skill": "Earthquake",
        "skill_damage": 22,
        "skill_count": 3,
        "gold": 0
    }
}

enemy_stats = {
    1: {
        "name": "Banak and Nakba",
        "hp": 25,
        "atk": 18,
        "def": 11,
    },

    2: {

    }
}

# sets
menu = ["1. Continue", "2. Exit"]

#Introduction of the game 
def intro():
    print("Welcome to the Encantadia! Traveler!")
    choice = input("Ready for an adventure? (YES or NO) ").upper()

    if choice == "YES":
        player = createPlayer()
        dungeonTutorial(player)
    else:
        print("You left the game!")

#Player information and stats
def createPlayer():

    print("\n===========================================")

    name = input("What is your name? ").capitalize()

    print("Choose your Brilyante:")

    action = int(input("1. Brilyante ng Apoy\n" \
    "2. Brilyante ng Tubig\n" \
    "3. Brilyante ng Hangin\n" \
    "4. Brilyante ng Lupa\n" \
    "Enter the number of your choice: "))

    if action in brilyante_stats:
        # Store chosen brilyante
        player = brilyante_stats[action].copy() #variable para sa dictionary
        player["plyr_name"] = name

        print(f"\nWelcome, {name}!")
        print(f"You chose Brilyante ng {player['name']}")

        print(f"\n===== {name} STATS =====")
        print(f"HP: {player['hp']}")
        print(f"ATK: {player['atk']}")
        print(f"Defense: {player['def']}")
        print(f"Special Skill: {player['skill']}")
        print(f"Skill Damage: {player['skill_damage']}")
        print(f"Skill Count: {player['skill_count']}")
        print(f"Gold: {player['gold']}")
    
        start = input("\nStart your journey? (YES or NO) ").upper()
        
        if start == "YES":
            return player
        else:
            intro()
    else:
        print("Not Applicable!")

# Battle System (Computation of damage and HP reduction)
def attack_system(attacker_atk, defender_defense, defender_hp):

    # compute damage
    damage = attacker_atk - defender_defense

    # prevent negative damage
    if damage < 1:
        damage = 1

    # reduce HP
    new_hp = defender_hp - damage

    return new_hp, damage

# Display player stats
def displayPlayerStat(player):
    print(f"\n===== YOUR STATS =====")
    print(f"Name: {player['plyr_name']}")
    print(f"Brilyante: {player['name']}")
    print(f"HP: {player['hp']}")
    print(f"ATK: {player['atk']}")
    print(f"Defense: {player['def']}")
    print(f"Special Skill: {player['skill']}")
    print(f"Skill Damage: {player['skill_damage']}")
    print(f"Skill Count: {player['skill_count']}")
    print(f"Gold: {player['gold']}")

# Display menu options
def displayMenu():
    for menu_item in menu:
        
        print(menu_item)

# Display shop options
def dungeonTutorial(player):
    print("\n===== DUNGEON TUTORIAL =====")

    enemy = enemy_stats[1]

    print(f"\nA wild {enemy['name']} appeared!\n")
    print(f"\nYour HP: {player['hp']}")
    print(f"{enemy['name']} HP: {enemy['hp']}\n")

    # TURN-BASED BATTLE
    while player['hp'] > 0 and enemy['hp'] > 0:

        print("Tutorial: Pick a number to start your turn.")
        print("\n===== YOUR TURN =====")
        print("1. Basic Attack")
        print("2. Special Skill")

        move = input("Choose attack: ")

        if move == "1":

            enemy['hp'], damage = attack_system(player['atk'], enemy['def'], enemy['hp'])
            enemy['hp'] = max(0, enemy['hp'])

            print(f"\nYou dealt {damage} damage!")
            print(f"\n{enemy["name"]} health is now {enemy["hp"]}")

        elif move == "2":

            enemy["hp"], damage = attack_system(player["skill_damage"], enemy["def"], enemy["hp"])
            enemy["hp"] = max(0, enemy["hp"])

            player["skill_count"]-= 1

            print(f"\nYou dealt {damage} damage!")
            print(f"\nEnemy health is now {enemy["hp"]}")
            print(f"Special Skill remaining: {player["skill_count"]}")

        else:
            print("Invalid move!")
            continue

        if enemy["hp"] == 0:
            print(f"\n{enemy['name']} was defeated!")
            break

        # ENEMY TURN
        print(f"\n===== {enemy['name'].upper()} TURN =====")

        player["hp"], enemy_damage = attack_system(enemy["atk"], player["def"], player["hp"])

        print(f"{enemy["name"]} attacked!")

        print(f"\n{enemy["name"]} dealt {enemy_damage} damage!")
        print(f"Your health is now {player["hp"]}")

        # SHOW HP
        print(f"\nYour HP: {player['hp']}")
        print(f"{enemy['name']} HP: {enemy['hp']}\n")

    if player["hp"] <= 0:
        print("\nGAME OVER!")
        return
    
    # Reward after defeating the enemy
    print("\nCongratulations!")
    print("You cleared the tutorial!")
    print("You earned 150 Gold\n\n")
    player['gold'] += 150

    displayPlayerStat(player)

    print("\nOnce you defeat a level, you may proceed to Shop")
    displayMenu()
    choice = int(input("Choose Action: "))
    
    match choice:
        case 1:
            actualGame(player)
        case 2:
            choice = input("Are you quitting the game? (YES or NO) ").upper()
            if choice == "NO":
                actualGame(player)
            else:
                exit()
                    
def actualGame(player):
    print("IT WORKEDDD!")
    # displayPlayerStat(player)
    
intro()
