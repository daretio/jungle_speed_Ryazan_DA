import pytest
from card import Card


def test_create_card_from_text():
    text = 'rc'
    card = Card.create(text)
    assert card.color == 'red'
    assert card.form == 'c'


def test_create_card_list_from_text():
    text = 'yc rc yh yo'
    cards = Card.card_list(text)
    assert len(cards) == 4
    assert all(isinstance(card, Card) for card in cards)


def test_all_cards_creation():
    all_cards = Card.all_cards()
    assert len(all_cards) == 72  # 4 colors * 18 forms
    assert all(isinstance(card, Card) for card in all_cards)

