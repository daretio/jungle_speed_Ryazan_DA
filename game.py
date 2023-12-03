import json

from card import Card
from deck import Deck, Heap
from hand import Hand
from player import Player


class Game:
    HAND_SIZE = 7
    DEFAULT_PLAYER_NAMES = ['Bob', 'Mike']

    def __init__(self, player_names: list[str] | None = None):
        if player_names is None:
            player_names = Game.DEFAULT_PLAYER_NAMES
        self.deck = Deck()
        self.players = [Player(name, self.deck.draw(Game.HAND_SIZE)) for name in player_names]
        self.player_index = 0
        self.heaps = [Heap([self.deck.draw()], player) for player in player_names]

    @staticmethod
    def create(game_dict: dict):
        g = Game([])    # без игроков
        g.deck = Deck.create(game_dict['deck'])
        g.heaps = [Heap.create(game_dict['heap'])]
        g.players = [Player(p) for p in game_dict['players']]
        g.player_index = int(game_dict['player_index'])
        return g

    @property
    def current_player(self):
        return self.players[self.player_index]

    def run(self):
        running = True
        top = self.players[self.player_index].play_card(self.players[self.player_index].hand)
        self.next_player()
        while running:
            past_top = top
            top = self.players[self.player_index].play_card(self.players[self.player_index].hand)
            print(f'Top: {top, past_top}')
            print(self.current_player)
            duel = self.current_player.is_duel(top, past_top)
            print(f'Is duel available: {duel}')
            if duel:
                # можно сыграть дуэль
                pass
            else:
                pass
            print(self.current_player)

            # проверяем условие победы, если победили, выходим с индексом игрока
            if self.current_player.check_win_condition():
                return

            self.next_player()
            print("--------------------------------")

    def next_player(self):
        """ Переходим к следующему игроку. """
        self.player_index = (self.player_index + 1) % len(self.players)

    def congratulations(self):
        print(f'THE END! Winner {self.current_player.name}')


def new_game():
    from random import seed
    seed(7)
    g = Game(['Bob', 'Mike'])
    g.run()
    g.congratulations()


def load_game(filename: str):
    with open('data.json') as fin:
        d2 = json.load(fin)
    print(d2)
    g = Game.create(d2)
    g.run()
    g.congratulations()


if __name__ == '__main__':
    load_game('data.json')


