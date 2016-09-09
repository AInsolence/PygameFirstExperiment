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

'''Create object with classes'''
class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.xpos = xpos
        self.ypos = ypos
        self.bitmap = pygame.image.load(filename)# get object image, where filename = path to image
        #self.bitmap.set_colorkey((0, 0, 0))# make sprites background color invisible
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
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False
    if hero.go_right:
        hero.xpos += 1
        if hero.xpos > win_width - 50:
            hero.go_right = False
    else:
        hero.xpos -= 1
        if hero.xpos < 0:
            hero.go_right = True
    if hero.go_down:
        hero.ypos += 1
        if hero.ypos > win_hight - 50:
            hero.go_down = False
    else:
        hero.ypos -= 1
        if hero.ypos < 0:
            hero.go_down = True    
    pygame.display.flip()# update all on the screen
    #screen.fill(background_color)
    window.blit(screen, (0,0))# display screen
    screen.blit(background_image, (0,0))# show background image
    pygame.time.delay(3)# delay time of all game process, argument in milliseconds
    hero.render()# show hero
    aim.render()# show aim
