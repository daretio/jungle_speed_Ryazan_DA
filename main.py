import pygame as pg
import random

pg.init()
screen_width, screen_height = 800, 600
FPS = 24    # frame per second
clock = pg.time.Clock()

# изображения
bg_img = pg.image.load('src/background.png')
icon_img = pg.image.load('src/logo.jpg')
card_images = []
card_images.append(pg.image.load("src/carteverso.png"))
for i in range(1, 69+1):
    # Формируйте путь к файлу изображения с использованием текущего индекса
    filename = f"src/carte{i}.png"

    # Загрузите изображение и добавьте его в список
    card = pg.image.load(filename)
    card_images.append(card)
card_images.append(pg.image.load("src/nocard.png"))
card_images.append(pg.image.load("src/totem.png"))
display = pg.display.set_mode((screen_width, screen_height))
pg.display.set_icon(icon_img)
pg.display.set_caption('Jungle Speed')

sys_font = pg.font.SysFont('arial', 34)
font = pg.font.Font('src/04B_19.TTF', 48)

# display.fill('blue', (0, 0, screen_width, screen_height))
display.blit(bg_img, (0, 0))        # image.tr

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    display.fill((255, 255, 255))

    pos = 100
    # Отобразите каждое изображение на экране
    for i, image in enumerate(card_images):
        display.blit(image, ((100 * i)%800, pos))
        if 100*i > 800:
            pos += 100
            i /= 8

    pg.display.flip()

pg.quit()


# import sys
#
# import pygame
# from pygame.locals import QUIT
#
# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello World!')

# while True:
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.quit()
#            sys.exit()
#    pygame.display.update()