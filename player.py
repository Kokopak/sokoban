#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from config import * 

class Player:
    def __init__(self):
        self.pos = {
            K_LEFT: pygame.image.load("img/mario_gauche.gif"),
            K_RIGHT: pygame.image.load("img/mario_droite.gif"),
            K_UP:    pygame.image.load("img/mario_bas.gif"),
            K_DOWN:   pygame.image.load("img/mario_haut.gif")
        }
        self.position = K_UP

    def drawPlayer(self, screen, x, y):
        screen.blit(self.pos[self.position], (x * SIZE, y * SIZE))

    def set_position(self, pos) :
        self.position = pos
