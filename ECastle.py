import random

from pico2d import *


class ECastle:
    image = None
    imagehp=None
    def __init__(self):
        self.x, self.y = 850, 100
        self.hp=1000

        if ECastle.image == None:
            ECastle.image = load_image('e_Castle.png')
        if ECastle.imagehp==None:
            ECastle.imagehp=load_image('hpimage.png')

    def draw(self):
        self.image.clip_draw(0, 0, 150, 150, self.x, self.y)
        self.imagehp.clip_draw(0, 0, int((20*self.hp)/100), 10, self.x, self.y + 100)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-75,self.y-75,self.x+75,self.y+75

    def handle_event(self, event):
        pass








