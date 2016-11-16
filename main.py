import game_framework
from pico2d import *
import collision
import start_state



name = "MainState"
image = None


def enter():
    global image
    open_canvas(400,600)
    image=load_image('mainimage.png')


def exit():
    global image
    del(image)
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
                if event.x > 125 and event.x <275:
                    if 599-event.y > 280 and 599-event.y < 360: #플레이
                        game_framework.change_state(collision)
                    elif 599-event.y > 150 and  599-event.y < 230: #옵션설정
                        pass
                    elif  599-event.y > 70 and  599-event.y < 150:
                        pass
                if event.x > 350 and event.x < 400:
                    if  599-event.y > 30 and  599-event.y < 80:
                        pass
                    elif  599-event.y > 100 and  599-event.y <160:
                        pass
                    elif  599-event.y > 175 and  599-event.y< 225: #상점
                        pass







def draw_bb():
    for i in range(10):
        for j in range(12):
            draw_rectangle(i*50,j*50,(i+1)*50,(j+1)*50)


def draw(frame_time):
    clear_canvas()
    image.draw(200,300)
    draw_bb()
    update_canvas()

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






