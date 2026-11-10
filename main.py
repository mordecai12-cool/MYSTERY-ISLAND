from game import new_game, move, pick_up, light_beacon

def main():
    name = input("What is your name? ").strip()
    player = new_game(name)
    print("Welcome, " + player["name"] + "!")
    while not player["game_over"]:
        print("Location: " + player["location"] + " | Energy: " + str(player["energy"]))
        choice = input("Choose: north, south, pick, light, quit > ").strip().lower()
        if choice == "quit":
            print("Goodbye!")
            break
        if choice == "north" or choice == "south":
            print(move(player, choice))
        elif choice == "pick":
            item = input("Pick up what? ").strip().lower()
            print(pick_up(player, item))
        elif choice == "light":
            print(light_beacon(player))
        else:
            print("Invalid choice. Please try again.")

    if player["won"]:
        print("You won! The beacon is lit and the rescue boat is coming.")
    elif player["game_over"]:
        print("You ran out of energy. You lose.")

    again = input("Play again? (y/n) ").strip().lower()
    if again == "y":
        main()

main()