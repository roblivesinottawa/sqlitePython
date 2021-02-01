# this file will be for user code. it will interact with the database file.

import database

# add a prompt
MENU_PROMPT = """ -- Choose Favorite Hero app -- 

Please choose one of these options:

1) Add a new hero.
2) See all heroes.
3) Find a hero by name.
4) See which hero is the best.
5) Exit.

Your selection: """


# this will be asking the user questions, getting input back, etc
def menu():
    connection = database.connect()
    database.create_table(connection)


    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            prompt_add_new_hero(connection)
        elif user_input == "2":
            prompt_see_all_heroes(connection)
        elif user_input == "3":
           prompt_find_hero(connection)
        elif user_input == "4":
            prompt_find_best_hero(connection)
        else:
            print("invalid input. please try again.")

def prompt_add_new_hero(connection):
    name = input("enter hero name: ")
    power = input("enter hero's power: ")
    rating = int(input("enter your rating score (0-100): "))

    database.add_hero(connection, name, power, rating)


def prompt_see_all_heroes(connection):
    heroes = database.get_all_heroes(connection)

    for hero in heroes:
        print(f"{hero[1]} {hero[2]} - {hero[3]}/100")

def prompt_find_hero(connection):
    name = input("enter hero's name to find: ")
    heroes = database.get_heroes_by_name(connection, name)

    for hero in heroes:
        print(f"{hero[1]} {hero[2]} - {hero[3]}/100")

def prompt_find_best_hero(connection):
    name = input("enter hero's name to find: ")
    best_hero = database.get_best_hero(connection, name)

    print(f"the best hero is {name}")

menu()