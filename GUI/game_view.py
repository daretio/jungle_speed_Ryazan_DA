import pygame

from GUI.card_view import ViewCard
from GUI.config import RSC
from GUI.fly_card import FlyCard
from GUI.userevent import *
from card import Card


class ViewGame:
    BACKGROUND_COLOR = RSC['img']['bg_color']
    TICK_MS = int(1000 / RSC['FPS'])   # милисекунд между тиками анимации
    TICK_ANIMATION_DURATION = int(1000 / TICK_MS) # за сколько тиков отработает онимация
    def __init__(self, size):
        # Одна карта, клик мыши левой кнопкой - переворот карты, a - select/unselect
        pygame.time.set_timer(ANIMATION, self.TICK_MS)
        self.size = self.width, self.height = size
        self.fly: FlyCard | None = None

    def draw(self, display: pygame.Surface):
        display.fill(self.BACKGROUND_COLOR, (0, 0, self.width, self.height))
        pygame.display.update()

    def dispatcher(self, event: pygame.event.Event):
        """ Разбор 1 события. """
        if event.type == FLY_END:
            # надо пинуть game и сказать, что пора переходить к следующей фазе игры
            print('END OF FLY>>>>>>>>>>>')
            self.fly = None

        # нужна анимация - тогда ничего, кроме анимации
        if self.fly and event.type == ANIMATION:
            self.fly.fly()
            return

        # по левому клику мыши - событие на карте
        if event.type == pygame.MOUSEBUTTONDOWN:
            key = pygame.mouse.get_pressed()    # key[0] - left, key[2] - right
            print(key)
            pos = pygame.mouse.get_pos()
            print(pos)




