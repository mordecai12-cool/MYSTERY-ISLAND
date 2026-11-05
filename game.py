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

def pick_up(player, item):
    if item in player["inventory"]:
        return "You already have the " + item + "."
    player["inventory"].append(item)
    return "You pick up the " + item + "."

def can_cross_bridge(player):
    return "rope" in player["inventory"]