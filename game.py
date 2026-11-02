def new_game(name):
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
    }

MAP = {
    "Beach": {"north": "Jungle"},
    "Jungle": {"south": "Beach", "north": "Cave"},
    "Cave": {"south": "Jungle"},
}
def move(player, direction):
    exits = MAP[player["location"]]
    if direction not in exits:
        return "You can't go that way."
    player["location"] = exits[direction]
    player["energy"] = player["energy"] - 1
    return "You walk to " + player["location"] + "."

# player = new_game("Ada")
# print(move(player, "north"))
# print(player)
# print(move(player, "east"))
# print(player)