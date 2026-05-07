#disctionaries
brilyante_stats = {
    1: {
        "name": "Apoy",
        "hp": 30,
        "atk": 15,
        "defense": 10,
        "skill": "Fireball",
        "skill_damage": 30,
        "skill_count": 3
    },

    2: {
        "name": "Tubig",
        "hp": 30,
        "atk": 14,
        "defense": 12,
        "skill": "Tsunami",
        "skill_damage": 28,
        "skill_count": 3
    },

    3: {
        "name": "Hangin",
        "hp": 30,
        "atk": 13,
        "defense": 11,
        "skill": "Tornado",
        "skill_damage": 26,
        "skill_count": 3
    },

    4: {
        "name": "Lupa",
        "hp": 30,
        "atk": 11,
        "defense": 15,
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
        "defense": 11,
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
        print(f"Defense: {player['defense']}")
        print(f"Special Skill: {player['skill']}")
        print(f"Skill Damage: {player['skill_damage']}")
        print(f"Skill Count: {player['skill_count']}")

        return player
    
        start = input("Start your journey?").upper()
        
        if start == "YES":
            dungeonStart()
        else:
            intro()


    else:
        print("Not Applicable!")

def gameIntro(choice):
    if choice == "YES":
        createPlayer()
    else:
        print("You left the game!")

def dungeonStart():
    print("\n===== DUNGEON START =====")

    
intro()
