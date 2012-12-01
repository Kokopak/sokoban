#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from grille import Grille
from player import Player

#------------
pygame.init()
screen = pygame.display.set_mode((408,408))
pygame.display.set_caption("Sokoban")
#------------

background = pygame.image.load("img/back.png")

screen.blit(background, (0,0))

_grille = Grille()
_grille.drawMap(screen)
_grille.genMap()

_player = Player(_grille)
_player.drawPlayer(screen)

pygame.display.flip()

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            _player.move(event.key)
    screen.blit(background, (0,0))
    _grille.drawMap(screen)
    _player.drawPlayer(screen)
    pygame.display.flip()
            
