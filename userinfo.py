import random

import json
import os
from pico2d import *
#font=None
#font = load_font('ENCR10B.TTF')
class user:
    HP, ATTACK = 0, 1

    def __init__(self):
        self.level=1
        self.gold=5000
        self.knight=[100,1]
        self.ninza=[100,1]
       # self.font=load_font('ENCR10B.TTF')

    def update(self, frame_time):
       pass


    def handle_event(self, event):
        pass

    def draw(self):
        pass
       # self.font.draw(50, 30, 'GOLD: %s' % self.gold)








