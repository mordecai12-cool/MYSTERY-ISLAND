import unittest
import sys
sys.path.insert(0, ".")
from game import new_game, move, pick_up, can_cross_bridge


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

    def test_rope_collected_once(self):
        player = new_game("Ada")
        pick_up(player, "rope")
        pick_up(player, "rope")
        self.assertEqual(player["inventory"], ["rope"])

    def test_bridge_blocked_without_rope(self):
        player = new_game("Ada")
        # use assertFalse on can_cross_bridge(player)
        self.assertFalse(can_cross_bridge(player))

    def test_bridge_open_with_rope(self):
        player = new_game("Ada")
        pick_up(player, "rope")
        # use assertTrue on can_cross_bridge(player)
        self.assertTrue(can_cross_bridge(player))

    def test_move_to_bridge_blocked_without_rope(self):
        player = new_game("Ada")
        player["location"] = "Cave"
        move(player, "north")
        # assertEqual: location should still be ???
        # assertEqual: energy should still be ???