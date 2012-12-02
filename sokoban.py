#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *

from grille import Grille
from player import Player
from config import *

pygame.init()
screen = pygame.display.set_mode((LARGEUR*SIZE, HAUTEUR*SIZE))
pygame.display.set_caption(TITRE)

background = pygame.image.load("img/back.png")

screen.blit(background, (0,0))

grille = Grille(screen, "lvl/lv1")
grille.drawMap()
pygame.display.flip()

continuer = True
while not grille.is_fini():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            grille.player_move(event.key)
    screen.blit(background, (0,0))
    grille.drawMap()
    pygame.display.flip()
