import game_framework
from pico2d import *
import collision
from userinfo import user
import main



name = "upgradeState"
upgrade = None
select=None


def enter():
    global upgrade,select
    global userlist
    userlist=user()
    open_canvas(400,600)
    upgrade=load_image('upgrade.png')
    select=load_image('upgradeselect.png')


def exit():
    global upgrade,select
    del(upgrade,select)
    close_canvas()


def handle_event(self, event):
    if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
        self.select(event.x, 599 - event.y)



def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if event.x > 0 and event.x <100:
                    if 599-event.y > 350 and 599-event.y < 450: #플레이
                        userlist.knight[userlist.HP]=50
                        print( userlist.knight[userlist.HP])
                    elif 599-event.y > 250 and  599-event.y < 350: #옵션설정
                        pass








def draw_bb():
    for i in range(10):
        for j in range(12):
            draw_rectangle(i*50,j*50,(i+1)*50,(j+1)*50)


def draw(frame_time):
    clear_canvas()
    upgrade.clip_draw(0, 0, 200, 50, 200, 550)
    select.clip_draw(0, 0, 100, 400, 50, 250)
    draw_bb()
    update_canvas()

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






