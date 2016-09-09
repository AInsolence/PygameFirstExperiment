#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import *
#main variables
win_width = 850
win_hight = 535
main_window = (win_width, win_hight)
#create window
window = pygame.display.set_mode(main_window)
pygame.display.set_caption('CAT The CATCHER!')
#create gameplay screen
background_image = pygame.image.load('image/firstStage_background.jpg')
screen = pygame.Surface((int(win_width - 10), int(win_hight - 10)))

'''Check collisions of objects in our game'''
def collide(object1, object2):
    if (object1.xpos > object2.xpos - object1.width) and (object1.xpos < object2.xpos + object1.width) and (object1.ypos > object2.ypos - object1.hight) and (object1.ypos < object2.ypos + object1.hight):
        return True
    return False

'''Create object with classes'''
class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.xpos = xpos
        self.ypos = ypos
        self.bitmap = pygame.image.load(filename)# get object image, where filename = path to image
        #self.bitmap.set_colorkey((0, 0, 0))# make sprites background color invisible if it exists
        height = 50
        width = 50
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))
'''Game objects'''
hero = Sprite(0, 0, 'image/monster5050.png')
aim = Sprite(50, 0, 'image/squeaky_mouse.png')
hero.go_right = True
hero.go_down = True

'''Main Game Loop'''
play = True
while play:
    for e in pygame.event.get():   # !!!EVENT Handler block!!!
        if e.type == pygame.QUIT:
            play = False
    if hero.go_right:
        hero.xpos += 1
        if hero.xpos > win_width - hero.width:
            hero.go_right = False
    else:
        hero.xpos -= 1
        if hero.xpos < 0:
            hero.go_right = True
    if hero.go_down:
        hero.ypos += 1
        if hero.ypos > win_hight - hero.hight:
            hero.go_down = False
    else:
        hero.ypos -= 1
        if hero.ypos < 0:
            hero.go_down = True   
    if collide(hero, aim):
        
            
    pygame.display.flip()# update all on the screen
    pygame.time.delay(3)# delay time of all game process, argument in milliseconds
    window.blit(screen, (0,0))# display screen
    screen.blit(background_image, (0,0))# show background image
    hero.render()# show hero
    aim.render()# show aim
