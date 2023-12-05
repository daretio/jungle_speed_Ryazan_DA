import random

from card import Card


class Deck:
    """ Колода карт"""

    def __init__(self, cards: list[Card] | None = None):
        if cards is None:
            self.cards = Card.all_cards()
            random.shuffle(self.cards)
        else:
            self.cards = cards

    def __repr__(self):
        """ rc yc bh bh """
        return ' '.join([str(c) for c in self.cards])

    def draw(self, n: int = 1):
        """ Взяли из колоды 1 карту и вернули ее."""
        if n == 1:
            return self.cards.pop()
        else:
            res = self.cards[-n:]
            self.cards = self.cards[:-n]
            return res

    @staticmethod
    def create(text: str):
        return Deck(Card.card_list(text))


class Heap:
    """Куча"""
    def __init__(self, cards=None, player=None):
        self.player = player
        self.cards = [] if cards is None else cards

    def __repr__(self):
        return repr(self.top()) if self.cards else 'Empty heap'

    def top(self) -> Card:
        """ Верхняя карта отбоя. """
        return self.cards[-1] if self.cards else None

    def put(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        """ Удаляет из кучи карту card """
        self.cards.remove(card)

    @staticmethod
    def create(text: str):
        return Heap(Card.card_list(text))


