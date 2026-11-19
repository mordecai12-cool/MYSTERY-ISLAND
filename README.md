# MYSTERY-ISLAND

# The Lost Lighthouse (Mystery Island)

A text adventure written in Python. You wake up on Mystery Island after a storm. The lighthouse is dark and the bridge is locked. Restore the beacon before you run out of energy to call the rescue boat.

## Prerequisites

- Python3 --version
- No external libraries. Only the Python standard library is used.

## How to run

```
python3 main.py
```

Enter your name, then type a command at each prompt.

## Controls

| Command | What it does |
|---------|--------------|
| `north` / `south` | Move to the next location |
| `pick`  | Asks for an item name (`lantern` or `rope`), then picks it up |
| `light` | Tries to light the beacon |
| `quit`  | Ends the current game |

Input is not case-sensitive and extra spaces are ignored.

## Game rules

- The map is a line: Beach, Jungle, Cave, Old Bridge, Lighthouse.
- You start at the Beach with 5 energy and an empty inventory.
- Every successful move costs 1 energy. Picking up items is free.
- Invalid input, wrong directions, refused pickups and blocked actions cost nothing and change nothing.
- The lantern lies at the Beach. The rope lies in the Cave.
- Each item can be picked up only once, and only where it lies.
- You cannot enter the Old Bridge without the rope.
- You can light the beacon only at the Lighthouse and only with the lantern. Doing so wins the game.
- If your energy reaches 0 before the beacon is lit, you lose.
- After the game ends, you can no longer move or act.
- The game is deterministic: the same state and action always give the same result.

## Example winning path

Inputs, in order:

```
pick
lantern
north
north
pick
rope
north
north
light
```

You finish with 1 energy left. One wasted move makes the game unwinnable.

## How to run tests

```
python3 -m unittest discover -s tests -v
```

There are 14 tests covering movement, energy, pickups, the bridge rule, the beacon rule, winning, losing, replay reset and invalid input.

## Project structure

- `game.py`: game rules (`new_game`, `move`, `pick_up`, `can_cross_bridge`, `can_light_beacon`, `light_beacon`). No printing or typing in the rules.
- `main.py`: the menu loop, input cleaning, messages and replay.
- `tests/test_game.py`: unit tests for the game rules.

## Known limitations

- Only `north` and `south` exist as directions.
- The "Play again?" question treats any answer except `y` as no.
- The name is asked again on every replay.
- An empty name is accepted.
- The `pick` command asks for the item name in a second prompt.
- There is only one winning path.