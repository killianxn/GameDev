#disctionaries
brilyante_stats = {
    1: {
        "name": "Apoy",
        "hp": 30,
        "atk": 15,
        "def": 10,
        "skill": "Fireball",
        "skill_damage": 30,
        "skill_count": 3
    },

    2: {
        "name": "Tubig",
        "hp": 30,
        "atk": 14,
        "def": 12,
        "skill": "Tsunami",
        "skill_damage": 28,
        "skill_count": 3
    },

    3: {
        "name": "Hangin",
        "hp": 30,
        "atk": 13,
        "def": 11,
        "skill": "Tornado",
        "skill_damage": 26,
        "skill_count": 3
    },

    4: {
        "name": "Lupa",
        "hp": 30,
        "atk": 11,
        "def": 15,
        "skill": "Earthquake",
        "skill_damage": 22,
        "skill_count": 3
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
def intro():
    print("Welcome to the Encantadia! Traveler!")
    choice = input("Ready for an adventure? (YES or NO)").upper()
    gameIntro(choice)

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
        player = brilyante_stats[action] #variable para sa dictionary

        print(f"\nWelcome, {name}!")
        print(f"You chose Brilyante ng {player['name']}")

        print(f"\n===== {name} STATS =====")
        print(f"HP: {player['hp']}")
        print(f"ATK: {player['atk']}")
        print(f"Defense: {player['def']}")
        print(f"Special Skill: {player['skill']}")
        print(f"Skill Damage: {player['skill_damage']}")
        print(f"Skill Count: {player['skill_count']}")
    
        start = input("Start your journey?").upper()
        
        if start == "YES":
            dungeonTutorial(player)
            return player
        else:
            intro()
    else:
        print("Not Applicable!")

def gameIntro(choice):
    if choice == "YES":
        createPlayer()
    else:
        print("You left the game!")

def attack_system(attacker_atk, defender_defense, defender_hp):

    # compute damage
    damage = attacker_atk - defender_defense

    # prevent negative damage
    if damage < 1:
        damage = 1

    # reduce HP
    new_hp = defender_hp - damage

    return new_hp, damage


def dungeonTutorial(player):
    print("\n===== DUNGEON TUTORIAL =====")

    enemy = enemy_stats[1]

    for enemy_id in enemy_stats:

        enemy = enemy_stats[1]

        print(f"\nA wild {enemy['name']} appeared!")

        # TURN-BASED BATTLE
        while player["hp"] > 0 and enemy["hp"] > 0:

            print("\n===== YOUR TURN =====")
            print("1. Basic Attack")
            print("2. Special Skill")

            move = input("Choose attack: ")

            if move == "1":

                enemy["hp"], damage = attack_system(player["atk"], enemy["def"], enemy["hp"])

                print(f"\nYou dealt {damage} damage!")
                print(f"\nEnemy health is now {enemy["hp"]}")

            elif move == "2":

                enemy["hp"], damage = attack_system(player["skill_damage"], enemy["def"], enemy["hp"])

                player["skill_count"]-= 1

                print(f"\nYou dealt {damage} damage!")
                print(f"\nEnemy health is now {enemy["hp"]}")
                print(f"Special Skill remaining: {player["skill_count"]}")
            else:
                print("finish na")
    
intro()
