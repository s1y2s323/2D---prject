import random

from pico2d import *



class bomb:
    image = None
    def __init__(self):
        self.x, self.y = 0,0
        if bomb.image == None:
            bomb.image = load_image('bomb.png')

    def update(self, frame_time):
        pass

    def set_x(self,x):
        self.x=x

    def set_y(self,y):
        self.y=y
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


    def draw(self):
        self.image.clip_draw(0, 0, 50, 50, self.x, self.y)


    def handle_event(self, event):
        pass

class cannon:
    image = None
    NORMAL, ATTACK = 0, 1
    def __init__(self):
        self.bullet=bomb() #대포(총알) 합성
        self.list=[]
        self.x, self.y = 30, 30
        self.t=0
        self.pointx, self.pointy=0,0
        self.state=0
        if cannon.image == None:
            cannon.image = load_image('cannon.png')


    def draw(self):
        self.image.clip_draw(0, 0, 50, 50, self.x, self.y)
        self.bullet.draw()

    def set_state(self,x,y):
        if x==self.ATTACK:
            self.state=self.ATTACK

        elif x==self.NORMAL:
            self.state=self.NORMAL


    def update(self,frame_time):
        if self.state==self.ATTACK:
            self.state=self.ATTACK
            if self.t >1:
                self.t=0
            self.t+=frame_time
            self.bullet.x = (1 - self.t) * (1 - self.t) * self.x + 2 * self.t * (1 - self.t) * (self.x + self.pointx) / 2 + self.t * self.t * self.pointx
            self.bullet.y = (1 - self.t) * (1 - self.t) * self.y + 2 * self.t * (1 - self.t) * 500 + self.t * self.t * self.pointy
        elif self.state==self.NORMAL:
            self.state=self.NORMAL
            if self.t > 0:
                self.t += frame_time
            if self.t > 1:
                self.pointx=30
                self.pointy=30
                self.t=0


    def set_point(self,x):
        (self.pointx,self.pointy)=x



    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.bullet.x-25 , self.bullet.y-25,self.bullet.x+25,self.bullet.y+25

    def handle_event(self, event):
        pass








