#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *

from grille import Grille
from player import Player
from config import *

pygame.init()
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption(TITRE)

background = pygame.image.load("img/back.png")

screen.blit(background, (0,0))

_grille = Grille("lvl/lv1")
_grille.drawMap(screen)

_player = Player(_grille)
_player.drawPlayer(screen)

pygame.display.flip()

continuer = True
while not _grille.is_fini():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            _player.move(event.key)
            if event.key == K_r:
                _grille.genMap("lvl/lv1")
                _grille.drawMap(screen)
                _player = Player(_grille)
                _player.drawPlayer(screen)
    screen.blit(background, (0,0))
    _grille.drawMap(screen)
    _player.drawPlayer(screen)
    pygame.display.flip()
            
