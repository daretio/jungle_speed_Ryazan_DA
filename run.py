#!/usr/bin/env python3
import pygame as pg
from game import Game


def main():
    pg.init()
    game = Game()
    game.new_game()
    pg.quit()


if __name__ == '__main__':
    main()