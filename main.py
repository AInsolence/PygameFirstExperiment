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
pygame.display.set_caption('Shoot!!!')
#create gameplay screen
background_image = pygame.image.load('image/firstStage_background.jpg')
screen = pygame.Surface((int(win_width), int(win_hight)))

'''Check collisions of objects in our game'''
def collide(object1, object2):
    if (object1.xpos > object2.xpos - object1.width) and (object1.xpos < object2.xpos + object1.width) and (object1.ypos > object2.ypos - object1.hight) and (object1.ypos < object2.ypos + object1.hight):
        return True
    return False

'''Create object with classes'''
class Sprite:
    def __init__(self, xpos = 0, ypos = 0, filename):
        self.xpos = xpos
        self.ypos = ypos
        self.bitmap = pygame.image.load(filename)# get object image, where filename = path to image
        #self.bitmap.set_colorkey((0, 0, 0))# make sprites background color invisible if it exists
        xwidth = 50
        yheight = 50
    def render(self):
        screen.blit(self.bitmap, (self.xpos, self.ypos))
'''Game objects'''
hero = Sprite((win_width/2), (win_hight + yheight), 'image/monster5050.png')
aim = Sprite(0, 100, 'image/squeaky_mouse.png')
aim.go_right = True
aim.go_down = False
bullet = Sprite(-10, 0, 'image/bullet.png')
bullet.xwidth = 20
bullet.yheight = 20
bullet.push = False

'''Key settings'''
pygame.key.set_repeat(1,1)

'''Main Game Loop'''
play = True
while play:
    for e in pygame.event.get():   # !!!EVENT Handler block!!!
        if e.type == pygame.QUIT:
            play = False
        '''Movements'''
        if e.type == pygame.KEYDOWN:
            '''Hero movements'''
            #x axis movement
            if e.key == pygame.K_LEFT:
                if hero.xpos != 0:
                    hero.xpos -= 1
            if e.key == pygame.K_RIGHT:
                if hero.xpos != win_width - hero.xwidth:
                    hero.xpos += 1  
            #y axis movement
            if e.key == pygame.K_UP:
                if hero.ypos != 150:
                    hero.ypos -= 1
            if e.key == pygame.K_DOWN:
                if hero.ypos != win_hight - hero.yheight:
                    hero.ypos += 1 
            '''Keybord buttons push events'''
            # bullet push
            if e.key == pygame.K_SPACE:
                if bullet.push == False:
                    bullet.xpos = hero.xpos + (hero.width/2)
                    bullet.push = True
        '''Collizion handler'''
        if collide(aim, bullet):
            bullet.push = False
            
    '''Aim movement block'''                
    if aim.go_right:
        aim.xpos += 1
        if aim.xpos > 800:
            aim.go_right = False
    else:
        aim.xpos -= 1
        if aim.xpos < 0:
            aim.go_right = True
    
    '''Bullet position block'''
    if bullet.ypos < 0:
        bullet.push = False
    if bullet.push == False:
        bullet.ypos = -10
    else:
        bullet.ypos -= 1
    
    
    '''Object reflection block'''
    pygame.display.flip()# update all on the screen
    pygame.time.delay(3)# delay time of all game process, argument in milliseconds
    window.blit(screen, (0,0))# display screen
    screen.blit(background_image, (0,0))# show background image
    hero.render()
    aim.render()
    bullet.render()
