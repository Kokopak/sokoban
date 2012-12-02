#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
from config import * 

class Grille:
    def __init__(self, fichier):
        self.ref_img = {
            MUR: pygame.image.load("img/mur.jpg"),
            CAISSE: pygame.image.load("img/caisse.jpg"),
            OBJECTIF: pygame.image.load("img/objectif.png"),
            CAISSE_OK: pygame.image.load("img/caisse_ok.jpg"),
        }
        with open (fichier, 'r') as fich:
            self.lvtest = [[int(l) for l in line.strip().split(" ")] for line in fich]

        self.coord_objec = []
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                if self.lvtest[y][x] == OBJECTIF :
                    self.coord_objec.append((x,y))


    def drawMap(self, screen):
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                img = self.lvtest[y][x]
                if img in (VIDE, PLAYER) :
                    x += 1
                else:
                    screen.blit(self.ref_img[img], (x*SIZE, y*SIZE))

    
    def getPlayerPosition(self, grille):
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                if self.lvtest[y][x] == PLAYER :
                    return (x*SIZE, y*SIZE)


    #---Déplacement des caisses ---#
    def moveCaisse(self, x, y, pos):
        self.is_fini()
        if pos == "gauche":
            if self.lvtest[y][x-2] not in (MUR, CAISSE, CAISSE_OK):
                if self.lvtest[y][x-1] == CAISSE_OK:
                    self.lvtest[y][x-1] = OBJECTIF
                else:
                    self.lvtest[y][x-1] = VIDE
                if self.lvtest[y][x-2] == OBJECTIF:
                    self.lvtest[y][x-2] = CAISSE_OK
                    return True
                else:
                    self.lvtest[y][x-2] = CAISSE
                    return True

        if pos == "droite":
            if self.lvtest[y][x+2] not in (MUR, CAISSE, CAISSE_OK):
                if self.lvtest[y][x+1] == CAISSE_OK:
                    self.lvtest[y][x+1] = OBJECTIF
                else:
                    self.lvtest[y][x+1] = VIDE
                if self.lvtest[y][x+2] == OBJECTIF:
                    self.lvtest[y][x+2] = CAISSE_OK
                    return True
                else:
                    self.lvtest[y][x+2] = CAISSE
                    return True

        if pos == "haut":
            if self.lvtest[y-2][x] not in (MUR, CAISSE, CAISSE_OK):
                if self.lvtest[y-1][x] == CAISSE_OK:
                    self.lvtest[y-1][x] = OBJECTIF
                else:
                    self.lvtest[y-1][x] = VIDE
                if self.lvtest[y-2][x] == OBJECTIF:
                    self.lvtest[y-2][x] = CAISSE_OK
                    return True
                else:
                    self.lvtest[y-2][x] = CAISSE
                    return True

        if pos == "bas":
            if self.lvtest[y+2][x] not in (MUR, CAISSE, CAISSE_OK):
                if self.lvtest[y+1][x] == CAISSE_OK:
                    self.lvtest[y+1][x] = OBJECTIF
                else:
                    self.lvtest[y+1][x] = VIDE
                if self.lvtest[y+2][x] == OBJECTIF:
                    self.lvtest[y+2][x] = CAISSE_OK
                    return True
                else:
                    self.lvtest[y+2][x] = CAISSE
                    return True
        return False

    def is_fini(self):
        lis = [self.lvtest[y][x] for (x, y) in self.coord_objec]
        return lis.count(CAISSE_OK) == len(self.coord_objec)

if __name__ == '__main__' :
    g = Grille()
    g.genMap("lv1")
