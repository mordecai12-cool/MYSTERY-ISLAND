# AI Learning Log: The Lost Lighthouse

Repository: https://github.com/mordecai12-cool/MYSTERY-ISLAND
Python version: python3 --version

---

## Entry 1: `input()` always returns a string

**Topic:** Variables, types and `input()` (Lesson 1)

**What the AI said:** When a user types `3`, `input()` gives back the text `"3"`, not the number 3. So `"3" + "3"` joins the two strings, and a menu comparison like `choice == 2` can never be true.

**My experiment:** I predicted this code would print `int` and then `6`:

```python
answer = input("Pick a number: ")
print(type(answer))
print(answer + answer)
```

I typed 3 and ran it. It printed `<class 'str'>` and then `33`. My prediction was wrong. I also tested `"5" == 5` (False) and `int("5") == 5` (True).

**My conclusion:** Python receives keyboard input as text. In my game, I compare the menu input to strings such as `"north"` and `"quit"`, and I clean it with `.strip().lower()` so `" NORTH "` still works. I avoid `int()` on menu input, because `int("banana")` would crash the program.

---

## Entry 2: A new game must create a new list

**Topic:** Lists, references and replay (Lesson 5, test T10)

**What the AI said:** A variable is a name that points to a value. Two names can point to the same list, so changing one changes what the other shows. Because of this, replay must build a brand new inventory instead of reusing the old one.

**My experiment:** First I predicted that this prints `["map", "rope"]`, and I was right:

```python
inventory = ["map"]
backpack = inventory
backpack.append("rope")
print(inventory)
```

Then in `main.py` I set `player["energy"] = 2`, printed it, called `player = new_game(name)` again, and printed the energy. The output was `2`, then `5`. I also played a full win, answered `y` to replay, and the new game started at the Beach with energy 5 and no items.

**My conclusion:** Every call to `new_game` builds a fresh dictionary and a fresh empty list, so nothing from the previous game can leak into the next one. I wrote `test_new_game_resets_state` to prove it.

---

## Entry 3 (bonus): A test caught a rule change

**Topic:** Automated tests (Lesson 7)

**What the AI said:** Tests exist to catch you when a rule changes.

**My experiment:** I made `pick_up` check where an item lies (the rope in the Cave, the lantern at the Beach). I ran the tests and three failed: `test_bridge_open_with_rope`, `test_beacon_lights_with_lantern` and `test_win_at_lighthouse_with_lantern`. They failed because they picked up items in the wrong place.

**My conclusion:** The code was fine and the old tests were wrong. I fixed them by setting the location first, and by picking up the lantern at the Beach before moving to the Lighthouse. The order of those two lines matters. All tests passed again.

---

## The concept I understand now that I didn't before

The concept I understand now that I didn't before is that the game's state (location, energy, inventory) lives in one dictionary, and the rules live in functions that return values instead of printing. Because `move` returns text and changes the state, a test can check it without any typing, and `main.py` only handles input and output.