import time

import pygame
from pygame import Surface, SurfaceType

from GUI.config import RSC, GEOM
from GUI.game_view import ViewGame
from GUI.userevent import ANIMATION


class Application:

    def __init__(self, pind1 = None, pind2 = None):
        pygame.init()
        self.size = (self.width, self.height) = GEOM['display']

        self.FPS = RSC['FPS']
        self.clock = pygame.time.Clock()

        self.pind1 = pind1 if not None else None
        self.pind2 = pind2 if not None else None
        self.totem = pygame.image.load(RSC['img']['totem'])

        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption(RSC['title'])
        pygame.display.set_icon(pygame.image.load(RSC['img']['logo']))

        self.vgame = ViewGame(self.size)

    def run(self):
        i = 0
        while i < 5000:  # ждём 5 секунд
            self.vgame.draw(self.display)
            self.display.blit(self.totem, (20, 20)) # ??
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Если нажали на крестик - победитель определяется рандомно
                    from random import randint
                    random_number = randint(-100, 100)
                    if random_number % 2 == 0:
                        return self.pind1, self.pind2
                    else:
                        return self.pind2, self.pind1
                if event.type == pygame.MOUSEBUTTONUP:  # Если успели кликнуть за 5 секунд - выигрывает первый игрок
                    return self.pind1, self.pind2
                self.vgame.dispatcher(event)
            time.sleep(0.001)
            i += 1
        pygame.quit()
        return self.pind2, self.pind1  # Если не успели кликнуть за 5 секунд - выигрывает второй игрок


app = Application()
app.run()
