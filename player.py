#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from grille import Grille
from config import * 


class Player:
    def __init__(self, grille):
        self.gauche = pygame.image.load("img/mario_gauche.gif")
        self.droite = pygame.image.load("img/mario_droite.gif")
        self.bas = pygame.image.load("img/mario_bas.gif")
        self.haut = pygame.image.load("img/mario_haut.gif")

        self.position = self.droite
        
        self.grille = grille
        self.pos = self.grille.getPlayerPosition(self.grille)

        self.x = self.pos[0]/SIZE 
        self.y = self.pos[1]/SIZE

    def drawPlayer(self, screen):
        screen.blit(self.position, (self.x * SIZE, self.y * SIZE))

    def move(self, key):
        if key == K_LEFT:
            self.position = self.gauche
            if not self.checkCollision():
                self.x -= 1
        elif key == K_RIGHT:
            self.position = self.droite
            if not self.checkCollision():
                self.x += 1
        elif key == K_UP:
            self.position = self.haut
            if not self.checkCollision():
                self.y -= 1
        elif key == K_DOWN:
            self.position = self.bas
            if not self.checkCollision():
                self.y += 1

    def checkCollision(self):
        self.hauty = self.y - 1
        self.basy = self.y + 1
        self.droitex = self.x + 1
        self.gauchex = self.x - 1
        
        for y in range(len(self.grille.lvtest)):
            for x in range(len(self.grille.lvtest[y])):
                if self.position == self.gauche:
                    pos_grille = self.grille.lvtest[self.y][self.gauchex]
                    if pos_grille == CAISSE or pos_grille == CAISSE_OK:
                        a = self.grille.moveCaisse(self.x, self.y, "gauche")
                        if a:
                            self.x = self.gauchex
                    return pos_grille == MUR or pos_grille == CAISSE or pos_grille == CAISSE_OK
                elif self.position == self.droite:
                    pos_grille = self.grille.lvtest[self.y][self.droitex]
                    if  pos_grille == CAISSE or pos_grille == CAISSE_OK:
                        a = self.grille.moveCaisse(self.x, self.y, "droite")
                        if a:
                            self.x = self.droitex
                    return pos_grille == MUR or  pos_grille == CAISSE or pos_grille == CAISSE_OK
                elif self.position == self.haut:
                    pos_grille = self.grille.lvtest[self.hauty][self.x]
                    if  pos_grille == CAISSE or pos_grille == CAISSE_OK:
                        a = self.grille.moveCaisse(self.x, self.y, "haut")
                        if a:
                            self.y = self.hauty
                    return pos_grille == MUR or  pos_grille == CAISSE or pos_grille == CAISSE_OK
                elif self.position == self.bas:
                    pos_grille = self.grille.lvtest[self.basy][self.x]
                    if  pos_grille == CAISSE or pos_grille == CAISSE_OK:
                        a = self.grille.moveCaisse(self.x, self.y, "bas")
                        if a:
                            self.y = self.basy
                    return pos_grille == MUR or  pos_grille == CAISSE or pos_grille == CAISSE_OK
