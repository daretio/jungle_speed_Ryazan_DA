
from card import Card
from hand import Hand


class Player:
    def __init__(self, name: str, hand: Hand | None = None):
        self.name = name
        self.hand = Hand([] if hand is None else hand)

    def __repr__(self):
        return f'{self.name}: {self.hand}'

    def add_card(self, card: Card):
        self.hand.add_card(card)

    def check_win_condition(self) -> bool:
        return len(self.hand) == 0

    def play_card(self, cards: list[Card]) -> Card:
        """ играет карту, удаляя ее из руки. Возвращает сыгранную карту. """
        card = cards[0]
        #print(self.hand, type(self.hand))
        self.hand.remove_card(card)
        return card

    @staticmethod
    def create(player_dict: dict):
        """ {'name': 'Bob', 'hand': 'rc bq yl'} """
        return Player(player_dict['name'], Hand.create(player_dict['hand']))

    @staticmethod
    def is_duel(card, past_card):
        """ Возвращает True, если возможна дуэль двух игроков"""
        return card.form == past_card.form

