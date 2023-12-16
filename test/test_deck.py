import unittest
from deck import Deck, Heap
from card import Card


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck([Card('red', 'h'), Card('green', 'h'), Card('blue', 's')])

    def test_init_with_cards(self):
        cards = [Card('red', 'h'), Card('green', 'h'), Card('blue', 's')]
        deck = Deck(cards)
        self.assertEqual(deck.cards, cards)

    def test_init_without_cards(self):
        deck = Deck()
        self.assertGreater(len(deck.cards), 0)

    def test_draw_one_card(self):
        drawn_card = self.deck.draw()
        self.assertEqual(drawn_card, Card('blue', 's'))
        self.assertEqual(len(self.deck.cards), 2)

    def test_create_from_text(self):
        card_text = 'rc yh gh'
        deck_from_text = Deck.create(card_text)
        self.assertEqual(len(deck_from_text.cards), 3)
        self.assertIsInstance(deck_from_text.cards[0], Card)


class TestHeap(unittest.TestCase):

    def setUp(self):
        self.heap = [Card('red', 'h'), Card('green', 'h'), Card('blue', 's')]

    def test_init_with_cards(self):
        cards = [Card('red', 'h'), Card('green', 'h'), Card('blue', 's')]
        heap = Heap(cards)
        self.assertEqual(heap.cards, cards)

    def test_init_without_cards(self):
        heap = Heap()
        self.assertEqual(len(heap.cards), 0)

    def test_remove_card(self):
        card_to_remove = Card('red', 'h')
        heap = Heap([card_to_remove, Card('yellow', 's')])
        heap.remove_card(card_to_remove)
        self.assertNotIn(card_to_remove, heap.cards)

    def test_create_from_text(self):
        card_text = 'rc yh gh'
        heap_from_text = Heap.create(card_text)
        self.assertEqual(len(heap_from_text.cards), 3)
        self.assertIsInstance(heap_from_text.cards[0], Card)


if __name__ == '__main__':
    unittest.main()
