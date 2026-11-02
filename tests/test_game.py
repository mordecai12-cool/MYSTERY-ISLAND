import unittest
import sys
sys.path.insert(0, ".")
from game import new_game, move


class TestMove(unittest.TestCase):
    def test_legal_move_costs_one_energy(self):
        player = new_game("Ada")
        move(player, "north")
        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 4)

    def test_wrong_direction_costs_nothing(self):
        player = new_game("Ada")
        move(player, "east")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)