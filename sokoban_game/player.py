#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from grille import Grille


class Player:
    def __init__(self, grille):
        self.gauche = pygame.image.load("img/mario_gauche.gif")
        self.droite = pygame.image.load("img/mario_droite.gif")
        self.bas = pygame.image.load("img/mario_bas.gif")
        self.haut = pygame.image.load("img/mario_haut.gif")

        self.position = self.droite
        
        self.grille = grille
        self.pos = self.grille.getPlayerPosition(self.grille)

        self.x = self.pos[0] 
        self.y = self.pos[1]

    def drawPlayer(self, screen):
        screen.blit(self.position, (self.x, self.y))

    def move(self, key):
        if key == K_LEFT:
            self.position = self.gauche
            if not self.checkCollision():
                self.x -= 34
        elif key == K_RIGHT:
            self.position = self.droite
            if not self.checkCollision():
                self.x += 34
        elif key == K_UP:
            self.position = self.haut
            if not self.checkCollision():
                self.y -= 34
        elif key == K_DOWN:
            self.position = self.bas
            if not self.checkCollision():
                self.y += 34

    def checkCollision(self):
        self.hauty = self.y - 34
        self.basy = self.y + 34
        self.droitex = self.x + 34
        self.gauchex = self.x - 34
        
        for y in range(len(self.grille.lvtest)):
            for x in range(len(self.grille.lvtest[y])):
                if self.position == self.gauche:
                    pos_grille = self.grille.lvtest[self.y/34][self.gauchex/34]
                    if pos_grille == 2 or pos_grille == 5:
                        self.grille.moveCaisse(self.x, self.y, "gauche")
                    return pos_grille == 1 or pos_grille == 2
                elif self.position == self.droite:
                    pos_grille = self.grille.lvtest[self.y/34][self.droitex/34]
                    if pos_grille == 2 or pos_grille == 5:
                        self.grille.moveCaisse(self.x, self.y, "droite")
                    return pos_grille == 1 or pos_grille == 2
                elif self.position == self.haut:
                    pos_grille = self.grille.lvtest[self.hauty/34][self.x/34]
                    if pos_grille == 2 or pos_grille == 5:
                        self.grille.moveCaisse(self.x, self.y, "haut")
                    return pos_grille == 1 or pos_grille == 2
                elif self.position == self.bas:
                    pos_grille = self.grille.lvtest[self.basy/34][self.x/34]
                    if pos_grille == 2 or pos_grille == 5:
                        self.grille.moveCaisse(self.x, self.y, "bas")
                    return pos_grille == 1 or pos_grille == 2
