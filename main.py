from game import new_game, move, pick_up, light_beacon


def main():
    name = input("What is your name? ").strip()
    player = new_game(name)
    print("Welcome, " + player["name"] + "!")


main()