#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import *
#main variables
win_width = 800
win_hight = 640
main_window = (win_width, win_hight)
background_color = '#A3FAA0'
#create window
window = pygame.display.set_mode(main_window)
pygame.display.set_caption('Hello PyGamers!')
#create gameplay screen
screen = pygame.Surface(win_width - 10, win_hight - 10)
screen.fill(Color(background_color))
#create main game loop
play = True
while play:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False
    
    window.blit(screen, (0,0))
    pygame.display.flip()