from card import Card
from deck import Heap


class Hand:
    """ Рука игрока"""
    def __init__(self, cardlist: list[Card] | None = None):
        self.cards = [] if cardlist is None else cardlist

    def __repr__(self):
        """ rc yc bh bh """
        return ' '.join([str(c) for c in self.cards])

    def __len__(self):
        """ Возвращает размер руки."""
        return len(self.cards)

    def __getitem__(self, item):
        """дает hand[i] и hand[i:j]"""
        return self.cards[item]

    def remove_card(self, card: Card):
        """ Удаляет из руки карту card (чтобы положить ее в отбой)"""
        self.cards.remove(card)
        # self.cards = [c for c in self.cards if c != card]

    def add_card(self, card: Card):
        """ Добавляет карту в руку. """
        self.cards.append(card)

    def move_cards(self, heap: Heap) -> None:
        """ Перемещает колоду карт от одного игрока к другому """
        for card in heap.cards:
            self.add_card(card)
            heap.remove_card(card)

    @staticmethod
    def create(text: str):
        return Hand(Card.card_list(text))

