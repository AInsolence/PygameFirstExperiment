#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import *
#main variables
win_width = 850
win_hight = 535
main_window = ((win_width - 10), (win_hight - 10))
#create window
window = pygame.display.set_mode(main_window)
pygame.display.set_caption('My First Game!!!')
#create gameplay screen
background_image = pygame.image.load('image/firstStage_background.jpg')
screen = pygame.Surface((win_width, win_hight))

'''Check collisions of objects in our game'''
def collide(object1, object2):
    if ((object1.xpos > object2.xpos - object1.xwidth) and (object1.xpos < object2.xpos + object2.xwidth) and (object1.ypos > object2.ypos - object1.yheight) and (object1.ypos < object2.ypos + object1.yheight)):
        return True
    return False

'''Create object with classes'''
class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.xpos = xpos
        self.ypos = ypos
        self.bitmap = pygame.image.load(filename)# get object image, where filename = path to image
        #self.bitmap.set_colorkey((0, 0, 0))# make sprites background color invisible if it exists
    xwidth = 60
    yheight = 50
    def render(self):
        screen.blit(self.bitmap, (self.xpos, self.ypos))
'''Game objects'''
hero = Sprite((win_width/2), (win_hight - 100), 'image/starship_1.PNG')
aim = Sprite(0, 100, 'image/enemy_ship_1.png')
aim.xwidth = 100
aim.yheight = 50
aim.go_right = True
aim.go_down = False
aim.speed = 1
bullet = Sprite(win_hight - 60, (hero.xpos - 25), 'image/bullet.png')
bullet.xwidth = 10
bullet.yheight = 10
bullet.push = False

'''Key settings'''
pygame.key.set_repeat(1,1)

'''Main Game Loop'''
play = True
scores = 0
while play:
    for e in pygame.event.get():   # !!!EVENT Handler block!!!
        if e.type == pygame.QUIT:
            print ('Your record is ', scores, ' scores!!!', '\n', 'Congratulations!')
            print ('Your best level is ', int(level + 1))
            play = False
        '''Movements'''
        if e.type == pygame.KEYDOWN:
            '''Hero movements'''
            #x axis movement
            if e.key == pygame.K_LEFT:
                if hero.xpos > 0:
                    hero.xpos -= 3
            if e.key == pygame.K_RIGHT:
                if hero.xpos < win_width - hero.xwidth - 10:
                    hero.xpos += 3  
            #y axis movement
            if e.key == pygame.K_UP:
                if hero.ypos >= win_hight - 200:
                    hero.ypos -= 3
            if e.key == pygame.K_DOWN:
                if hero.ypos <= win_hight - hero.yheight - 40:
                    hero.ypos += 3 
            '''Keybord buttons push events'''
            # bullet push
            if e.key == pygame.K_SPACE:
                if bullet.push == False:
                    bullet.xpos = hero.xpos + (hero.xwidth/2)
                    bullet.ypos = hero.ypos + (hero.yheight/2)
                    bullet.push = True
    '''Collizion handler'''
    if collide(aim, bullet):
        bullet.push = False
        scores += 10    
            
    '''Aim movement block'''                
    if aim.go_right:
        aim.xpos += aim.speed
        if aim.xpos > 730:
            aim.go_right = False
    else:
        aim.xpos -= aim.speed
        if aim.xpos < 0:
            aim.go_right = True
    
    '''Bullet position block'''
    if bullet.ypos < 0:
        bullet.push = False
    if bullet.push == False:
        bullet.ypos = win_hight
    else:
        bullet.ypos -= 5
    
    '''Difficalty level'''
    level = int(scores/30)
    aim.speed = level + 1

    
    '''Object reflection block'''
    pygame.display.flip()# update all on the screen
    pygame.time.delay(1)# delay time of all game process, argument in milliseconds
    window.blit(screen, (0,0))# display screen
    screen.blit(background_image, (0,0))# show background image
    bullet.render()
    hero.render()
    aim.render()