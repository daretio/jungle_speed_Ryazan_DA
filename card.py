import pytest


class Card:
    COLORS = ['red', 'green', 'blue', 'yellow']
    FORMS = ['circles', 'hexogonal', 'outline-circles', 'quatrogonal',
             'quatrogonal-with-points', 'quatrostars', 'snake',
             'cycle-snake', 'inner-x-circle', 'w-snake', '88-snake',
             'x-circle', 'inner-button', 'button', 'square-between-circles',
             'circle-between-squares', 'square-between-rectangles',
             'circle-between-rectangles']
    COLOR_LETTERS = {'r': 'red', 'g': 'green', 'b': 'blue', 'y': 'yellow'}
    FORM_LETTERS = {'c': 'circles', 'h': 'hexogonal', 'o': 'outline-circles', 'q': 'quatrogonal',
                    'p': 'quatrogonal-with-points', 's': 'quatrostars', 'n': 'snake', 'y': 'cycle-snake',
                    'i': 'inner-x-circle', 'w': 'w-snake', 'e': '88-snake', 'x': 'x-circle',
                    'u': 'inner_button', 'b': 'button', 'a': 'square-between-circles',
                    'd': 'circle-between-squares', 'r': 'square-between-rectangles', 'l': 'circle-between-rectangles'}

    def __init__(self, color, form):
        if color in self.COLORS:
            self.color = color  # 'red' vs 'r'
        else:
            raise ValueError(f'Wrong color {color}')

        if form in self.FORM_LETTERS:
            self.form = form
        else:
            raise ValueError(f'Wrong form {form}')

    def __repr__(self):
        return f'{self.color}{self.form}'

    def __eq__(self, other):
        return self.color == other.color and self.form == other.form

    @staticmethod
    def create(text: str):
        """ По тексту вида 'rc' возвращается карта Card('red', 'c')."""
        letter = Card.COLOR_LETTERS.get(text[0], None)
        form = text[1:]
        return Card(letter, form)

    @staticmethod
    def card_list(text: str):
        """ Из строки вида 'yc rc yh yo' возвращает список соответствующих карт."""
        return [Card.create(word) for word in text.split()]

    @staticmethod
    def all_cards():
        """ Все карты для создания колоды. """
        return [Card(color, form) for form in Card.FORM_LETTERS for color in Card.COLORS]




