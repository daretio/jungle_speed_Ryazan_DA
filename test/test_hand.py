import unittest
from hand import Hand
from card import Card
from deck import Heap


class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand([Card('red', 'h'), Card('green', 'h'), Card('blue', 's')])

    def test_add_card(self):
        new_card = Card('blue', 's')
        self.hand.add_card(new_card)
        self.assertIn(new_card, self.hand.cards)

    def test_remove_card(self):
        card_to_remove = self.hand.cards[0]
        self.hand.remove_card(card_to_remove)
        self.assertNotIn(card_to_remove, self.hand.cards)

    def test_move_cards(self):
        heap = Heap([Card('red', 's'), Card('yellow', 's')])
        initial_hand_length = len(self.hand.cards)
        initial_heap_length = len(heap.cards)
        self.hand.move_cards(heap)
        self.assertEqual(len(self.hand.cards), initial_hand_length + initial_heap_length - 1)
        self.assertEqual(len(heap.cards), 1)

    def test_create_from_text(self):
        hand_from_text = Hand.create('rs gh bh')
        self.assertEqual(len(hand_from_text.cards), 3)
        self.assertIsInstance(hand_from_text.cards[0], Card)

    def test_get_item(self):
        self.assertEqual(self.hand[0], Card('red', 'h'))
        self.assertEqual(self.hand[1:3], [Card('green', 'h'), Card('blue', 's')])


if __name__ == '__main__':
    unittest.main()
