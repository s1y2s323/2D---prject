import game_framework
from pico2d import *
import main


name = "TitleState"
image = None


def enter():
    global image
    open_canvas(600,400)
    image=load_image('startimage.png')


def exit():
    global image
    del(image)
    close_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main)






def draw(frame_time):

    clear_canvas()
    image.clip_draw(0, 0, 600, 400, 300, 200)
    update_canvas()

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






