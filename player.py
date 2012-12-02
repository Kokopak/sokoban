#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from config import * 

class Player:
    def __init__(self):
        self.pos = {
            GAUCHE: pygame.image.load("img/mario_gauche.gif"),
            DROITE: pygame.image.load("img/mario_droite.gif"),
            BAS:    pygame.image.load("img/mario_bas.gif"),
            HAUT:   pygame.image.load("img/mario_haut.gif")
        }
        self.position = DROITE

    def drawPlayer(self, screen, x, y):
        screen.blit(self.pos[self.position], (x * SIZE, y * SIZE))

    def set_position(self, pos) :
        self.position = pos
