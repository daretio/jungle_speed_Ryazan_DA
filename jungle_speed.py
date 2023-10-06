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




def display_redraw():
    display.blit(bg_img, (0, 0))
    pg.display.update()

def event_processing():
    running = True
    for event in pg.event.get():
        # нажали крестик на окне
        if event.type == pg.QUIT:
            running = False
        # тут нажимаем на клавиши
        if event.type == pg.KEYDOWN:
            # нажали на q - quit
            if event.key == pg.K_q:
                running = False

    clock.tick(FPS)
    return running

# random.seed(77)
running = True
while running:
    display_redraw()
    running = event_processing()

pg.quit()