import unittest
import sys
sys.path.insert(0, ".")
from game import new_game, move, pick_up, can_cross_bridge, can_light_beacon, light_beacon


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
        player["location"] = "Cave"
        pick_up(player, "rope")
        pick_up(player, "rope")
        self.assertEqual(player["inventory"], ["rope"])

    def test_bridge_blocked_without_rope(self):
        player = new_game("Ada")
        self.assertFalse(can_cross_bridge(player))

    def test_bridge_open_with_rope(self):
        player = new_game("Ada")
        player["location"] = "Cave"
        pick_up(player, "rope")
        self.assertTrue(can_cross_bridge(player))

    def test_move_to_bridge_blocked_without_rope(self):
        player = new_game("Ada")
        player["location"] = "Cave"
        move(player, "north")
        self.assertEqual(player["location"], "Cave")
        self.assertEqual(player["energy"], 5)

    def test_beacon_blocked_without_lantern(self):
        player = new_game("Ada")
        player["location"] = "Lighthouse"
        self.assertFalse(can_light_beacon(player))

    def test_beacon_lights_with_lantern(self):
        player = new_game("Ada")
        pick_up(player, "lantern")
        player["location"] = "Lighthouse"
        self.assertTrue(can_light_beacon(player))

    def test_energy_exhaustion_causes_loss(self):
        player = new_game("Ada")
        player["energy"] = 1
        move(player, "north")
        self.assertEqual(player["energy"], 0)
        self.assertTrue(player["game_over"])

    def test_no_moves_after_game_over(self):
        player = new_game("Ada")
        player["game_over"] = True
        move(player, "north")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)

    def test_win_at_lighthouse_with_lantern(self):
        player = new_game("Ada")
        pick_up(player, "lantern")
        player["location"] = "Lighthouse"
        light_beacon(player)
        self.assertTrue(player["won"])
        self.assertTrue(player["game_over"])

    def test_no_win_at_beach_with_lantern(self):
        player = new_game("Ada")
        pick_up(player, "lantern")
        light_beacon(player)
        self.assertFalse(player["won"])
        self.assertFalse(player["game_over"])