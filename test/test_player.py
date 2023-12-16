import unittest
from player import Player
from card import Card
from hand import Hand


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.hand = Hand([Card('red', 'h'), Card('green', 'h'), Card('blue', 's')])
        self.player = Player('Alice', self.hand)

    def test_check_win_condition(self):
        self.assertFalse(self.player.check_win_condition())
        empty_hand = Hand([])
        empty_player = Player('Bob', empty_hand)
        self.assertTrue(empty_player.check_win_condition())

    def test_create_from_dict(self):
        player_dict = {'name': 'Charlie', 'hand': 'rc gs yh'}
        created_player = Player.create(player_dict)
        self.assertEqual(created_player.name, 'Charlie')
        self.assertEqual(len(created_player.hand.cards), 3)

    def test_is_duel(self):
        card1 = Card('red', 'h')
        card2 = Card('yellow', 'h')
        self.assertTrue(Player.is_duel(card1, card2))
        card3 = Card('yellow', 's')
        self.assertFalse(Player.is_duel(card1, card3))


if __name__ == '__main__':
    unittest.main()
