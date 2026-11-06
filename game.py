def new_game(name):
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False,
    }

MAP = {
    "Beach": {"north": "Jungle"},
    "Jungle": {"south": "Beach", "north": "Cave"},
    "Cave": {"south": "Jungle", "north": "Old Bridge"},
    "Old Bridge": {"south": "Cave", "north": "Lighthouse"},
    "Lighthouse": {"south": "Old Bridge"},
}
def move(player, direction):
    if player["game_over"]:
        return "The game is over."
    exits = MAP[player["location"]]
    if direction not in exits:
        return "You can't go that way."
    destination = exits[direction]
    if destination == "Old Bridge" and not can_cross_bridge(player):
        return "The bridge is too dangerous without a rope."
    player["location"] = exits[direction]
    player["energy"] = player["energy"] - 1
    if player["energy"] == 0:
        player["game_over"] = True
        return "You collapse from exhaustion. Game over."
    return "You walk to " + player["location"] + "."

def pick_up(player, item):
    if item in player["inventory"]:
        return "You already have the " + item + "."
    player["inventory"].append(item)
    return "You pick up the " + item + "."

def can_cross_bridge(player):
    return "rope" in player["inventory"]

def can_light_beacon(player):
    return player["location"] == "Lighthouse" and "lantern" in player["inventory"]