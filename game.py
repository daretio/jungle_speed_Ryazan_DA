import json
import time

from card import Card
from deck import Deck, Heap
from hand import Hand
from player import Player


class Game:
    HAND_SIZE = 12
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
        g = Game([])  # без игроков
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
        # Добавляем карту из колоды игрока в кучу
        self.heaps[self.player_index].put(
            self.players[self.player_index].play_card(
                self.players[self.player_index].hand))
        # Берём верхнюю карту из кучи игрока
        past_player_index = self.player_index
        self.next_player()
        print(past_player_index, self.player_index)
        while running:
            self.heaps[self.player_index].put(
                self.players[self.player_index].play_card(
                    self.players[self.player_index].hand))
            past_top = self.heaps[past_player_index].top()  # Верхняя карта прошлого игрока
            top = self.heaps[self.player_index].top()  # Верхняя карта текущего игрока
            print(f'Top: {top, past_top}')
            print(self.current_player)
            duel = self.current_player.is_duel(top, past_top)  # Если совпали формы карт, играем дуэль
            print(f'Is duel available: {duel}')
            if duel:
                # Можно сыграть дуэль
                winner, looser = self.winner_of_duel(past_player_index)
                print(f'Heap of the winner: {self.heaps[winner].cards}')
                self.players[looser].hand.move_cards(self.heaps[winner])
                print(f'Winner: {self.players[winner]}')
                print(f'Looser: {self.players[looser]}')

            # print(f'Current player: {self.current_player}')

            # Проверяем условие победы, если победили, выходим с индексом игрока
            if self.current_player.check_win_condition():
                return

            past_player_index = self.player_index
            self.next_player()
            print("--------------------------------")

    def winner_of_duel(self, other_player_index):
        """Реализация невозможна без графического интерфейса (тотема). В качестве временного решения - случайный выбор
        победителя и програвшего"""
        from random import randint
        random_number = randint(-100, 100)
        if random_number % 2 == 0:
            return self.player_index, other_player_index
        else:
            return other_player_index, self.player_index

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
