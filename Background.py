from pico2d import *


class background:
    image = None

    def __init__(self):
        self.x, self.y = 100, 550
        self.type=5
        if background.image == None:
            background.image = load_image('background.png')


    def draw(self):
        self.image.clip_draw(0, 0, 1000, 600, 500, 300)












