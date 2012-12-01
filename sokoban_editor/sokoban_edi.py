#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *

#------------
pygame.init()
screen = pygame.display.set_mode((408,408))
pygame.display.set_caption("Sokoban Editor")
#------------

background = pygame.image.load("img/back.png")

screen.blit(background, (0,0))

pygame.display.flip()

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    screen.blit(background, (0,0))
    pygame.display.flip()
            
