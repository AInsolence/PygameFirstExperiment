#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import *
#main variables
win_width = 800
win_hight = 640
main_window = (win_width, win_hight)

background_image = pygame.image.load('image/firstStage_background.jpg')
=======
background_color = (70, 30, 100)
>>>>>>> a1465e15a49400fc2558e5ac3883823a93fe7c81
square_x_pos = 0
square_go_right = True
square_y_pos = 0
square_go_down = True
#create window
window = pygame.display.set_mode(main_window)
pygame.display.set_caption('Hello PyGamers!')
#create gameplay screen
<<<<<<< HEAD
screen = pygame.Surface((int(win_width - 10), int(win_hight - 10)))
screen.fill(Color(background_color))
#create simple object
square = pygame.Surface((40, 40))
square.fill((50, 50, 50))
=======
screen = pygame.Surface((win_width, win_hight))
screen.fill(background_color)
#create simple object
square = pygame.Surface((40, 40))
square.fill((100, 0, 0))
>>>>>>> a1465e15a49400fc2558e5ac3883823a93fe7c81
'''Create object with classes'''
class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)# get object image, where filename = path to image
        self.bitmap.set_colorkey((0, 0, 0))# make sprites background color invisible
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))
#hero object
<<<<<<< HEAD
hero = Sprite(0, 0, 'image/cat_fight.png')
aim = Sprite(50, 0, 'image/squeaky_mouse.png')
=======
>>>>>>> a1465e15a49400fc2558e5ac3883823a93fe7c81
hero.go_right = True
hero.go_down = True

'''Main Game Loop'''
play = True
while play:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False
    if square_go_right:
        square_x_pos += 1
        if square_x_pos > 760:
            square_go_right = False
    else:
        square_x_pos -= 1
        if square_x_pos < 0:
            square_go_right = True
    if square_go_down:
        square_y_pos += 1
        if square_y_pos > 600:
            square_go_down = False
    else:
        square_y_pos -= 1
        if square_y_pos < 0:
            square_go_down = True        
    window.blit(screen, (0,0))# display screen
    pygame.display.flip()# update all on the screen
    screen.blit(square, (square_x_pos, square_y_pos))# display object
    pygame.time.delay(3)# delay time of all game process, argument in milliseconds
    hero.render()
    aim.render()
