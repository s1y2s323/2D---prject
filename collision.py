from pico2d import *

import os
import game_framework
import main




from Knight import knight # import Boy class from boy.py
from Castle import Castle
from ECastle import ECastle
from Select import Select
from Zombie import zombie
from Ninza import ninza
from Cannon import cannon
from userinfo import user
from Background import background

import time
createtime=0
font=None
n1=0
n2=0
name = "collision"



def create_world():
    global boy,castle,select,boy2,boy3,Ecastle
    global daepo
    global User
    global backimage

    boy=[]
    boy2=[]
    boy3=[]
    castle=Castle()
    Ecastle=ECastle()
    select=Select()
    daepo=cannon()
    User=user()
    backimage=background()


def destroy_world():
    global boy,castle,select,boy2,boy3,bom,User,backimage,Ecastle
    global daepo
    for Knight in boy:
        del(Knight)
    for Zombie in boy2:
        del(Zombie)
    for Ninza in boy3:
        del(Ninza)

    del(Ecastle)
    del(User)
    del(castle)
    del(select)
    del(daepo)
    del(backimage)


def enter():
    global font
    open_canvas(1000,600)
    game_framework.reset_time()
    create_world()

    font = load_font('ENCR10B.TTF')


def exit():
    global font
    destroy_world()
    close_canvas()
    del (font)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.button)== (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                select.handle_event(event)
                if select.type==1:
                    if User.gold > 100:
                        User.gold -= 100
                        boy.append(knight())

                   # boy2.append(zombie())
                   # boy2.append(zombie())
                elif select.type==2:
                    if User.gold > 150:
                        User.gold -= 150
                        boy.append(ninza())




def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a <left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def createobject():
    global createtime
    createtime=(createtime+1)%100
    if createtime==0:
        boy2.append(zombie())

   # print(createtime)

   # c_time =time.clock()
    #time.sleep(10)
    ##temp_time=int(c_time)
    ##temp_time = int(c_time)%10
    ##if temp_time ==0:
    ##    temp_Time=time.clock()
    ##    temp_time2=int(temp_Time)
   # print(c_time)
   # print(temp_time)

   # if temp_time % 5 ==0:

      #  boy.append(knight())





def update(frame_time):

    global n1,n2
    createobject()
    for Knight in boy:
        Knight.update(frame_time)
    for Zombie in boy2:
        Zombie.update(frame_time)
    for Ninza in boy3:
        Ninza.update(frame_time)

    daepo.update(frame_time)

    for boys2 in boy2:
       # daepo.set_state(daepo.NORMAL, None)
        if boys2.x<800 and daepo.state==daepo.NORMAL:
            daepo.set_point(boys2.get_xy())
            daepo.set_state(daepo.ATTACK,None)
            break

           #bom.update(frame_time)


    for boys in boy:
        boys.set_state(boys.RIGHT_RUN, None)
        for boys2 in boy2:
            if collide(boys,boys2)==False:# and boys.get_state()==boys.RIGHT_ATTACK:
                boys.set_state(boys.RIGHT_RUN, None)
            elif(collide(boys,boys2)):
                boys.set_state(boys.RIGHT_ATTACK,boys2)
                if (boys2.hp < 0):
                    boy2.remove(boys2)
                break
            if boys.y > boys2.y and boys.get_state==boys.RIGHT_RUN:
                boys.set_dirY(0)
                break
            elif boys.y < boys2.y and boys.get_state==boys.RIGHT_RUN:
                boys.set_dirY(1)
                break


    for boys2 in boy2:
        boys2.set_state(boys2.LEFT_RUN, None)
        for boys in boy:
            if collide(boys2, boys) == False:# and boys2.get_state() == boys2.LEFT_ATTACK:
                boys2.set_state(boys2.LEFT_RUN,None)
            elif(collide(boys2,boys)):
                boys2.set_state(boys2.LEFT_ATTACK,boys)

                if(boys.hp<0):
                    boy.remove(boys)
                break

    for boys2 in boy2:
        if collide(boys2,castle) == True:
            boys2.set_state(boys2.LEFT_ATTACK, castle)

    for boys in boy:
        if collide(boys,Ecastle)==True:
            boys.set_state(boys.RIGHT_ATTACK,Ecastle)
    if castle.hp < 0 or Ecastle.hp < 0 :
       # exit()
        game_framework.change_state(main)



       # exit()



def draw(frame_time):
    clear_canvas()
    backimage.draw()
   # font.draw( 50,  40, 'Time: %3.2f' % User.gold,(128,128,128))

    for Knight in boy:
        Knight.draw()
        #Knight.draw_bb()

    for Zombie in boy2:
        Zombie.draw()
       # Zombie.draw_bb()

    for Ninza in boy3:
        Ninza.draw()
       # Ninza.draw_bb()



    castle.draw()
    #castle.draw_bb()
    Ecastle.draw()
   # Ecastle.draw_bb()
    select.draw()
   # select.draw_bb()
    daepo.draw()
   # daepo.draw_bb()
    font.draw(850, 580, 'GOLD: %s' % User.gold)


    update_canvas()






