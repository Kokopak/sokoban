#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import time
from pygame.locals import *

from grille import Grille
from player import Player
from config import *

pygame.init()
screen = pygame.display.set_mode((LARGEUR*SIZE, HAUTEUR*SIZE))
pygame.display.set_caption(TITRE)

grille = Grille(screen, "lvl/lv1")
grille.drawMap()
pygame.display.update()
clock = pygame.time.Clock()
fps = 30

continuer = True
while continuer and not grille.is_fini():
    for event in pygame.event.get():
        if event.type == QUIT:
            print "Bye !"
            continuer = False
        if event.type == KEYDOWN:
            grille.player_move(event.key)
            pygame.display.update()
    clock.tick(fps)
