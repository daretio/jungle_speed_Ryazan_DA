import pygame as pg


class Game:
    current_scene_index = 0

    def __init__(self):
        self.scenes = []
        self.game_over = False
        self.screen_width, self.screen_height = 800, 600  # Инициализация размеров окна
        self.FPS = 24  # Частота обновления экрана
        self.clock = pg.time.Clock()

        # Инициализация изображений
        self.bg_img = pg.image.load('assets/src/background.png')  # Фон
        self.icon_img = pg.image.load('assets/src/logo.jpg')  # Лого
        self.card_images = [pg.image.load("assets/src/carteverso.png")]  # Карты
        for i in range(1, 69 + 1):
            filename = f"assets/src/carte{i}.png"
            card = pg.image.load(filename)
            self.card_images.append(card)
        self.card_images.append(pg.image.load("assets/src/nocard.png"))
        self.card_images.append(pg.image.load("assets/src/totem.png"))

        # Инициализация окна дисплея
        self.display = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_icon(self.icon_img)
        pg.display.set_caption('Jungle Speed')

        # Инициализация шрифта
        sys_font = pg.font.SysFont('arial', 34)
        font = pg.font.Font('assets/src/04B_19.TTF', 48)
        self.display.blit(self.bg_img, (0, 0))  # image.tr

    # Метод перезаливки дисплея
    def display_redraw(self):
        self.display.blit(self.bg_img, (0, 0))
        pg.display.update()

    def process_all_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Нажали крестик на окне
                self.game_over = True
            if event.type == pg.KEYDOWN:  # Тут нажимаем на клавиши
                if event.key == pg.K_q:  # Нажали на q - quit
                    self.game_over = True
        self.clock.tick(self.FPS)

    def main_loop(self) -> None:
        while not self.game_over:
            self.process_all_events()
            self.display_redraw()
            pg.time.wait(10)
