#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
from config import * 

class Grille:
    def __init__(self):
        objectif = pygame.image.load("img/objectif.png")
        caisse = pygame.image.load("img/caisse.jpg")
        caisse_ok = pygame.image.load("img/caisse_ok.jpg")
        mur = pygame.image.load("img/mur.jpg")
        back = pygame.image.load("img/back.jpg")

        self.ref_img = {1: mur, 2: caisse, 3: objectif, 5: caisse_ok}

        self.lvtest = []
        self.valide_caisse = False

    def genMap(self, fichier):
        with open (fichier, 'rb') as fich:
            self.lvtest = [[int(l) for l in line.strip().split(" ")] for line in fich]

        self.coord_objec = []
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                a = self.lvtest[y][x]
                if a == 3:
                    self.coord_objec.append((x*34,y*34))


    def drawMap(self, screen):
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                img = self.lvtest[y][x]
                if img == 0 or img == 4:
                    x += 1
                else:
                    screen.blit(self.ref_img[img], (x*34, y*34))

    
    def getPlayerPosition(self, grille):
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                if self.lvtest[y][x] == 4:
                    return (x*34, y*34)


    #---Déplacement des caisses ---#
    def moveCaisse(self, x, y, pos):
        self.is_fini()
        if pos == "gauche":
            if self.lvtest[y][(x-2)] != MUR and self.lvtest[y][(x-2)] != CAISSE and self.lvtest[y][(x-2)] != CAISSE_OK:
                if self.lvtest[y][(x-1)] == CAISSE_OK:
                    self.lvtest[y][(x-1)] = OBJECTIF
                else:
                    self.lvtest[y][(x-1)] = VIDE
                if self.lvtest[y][(x-2)] == OBJECTIF:
                    self.lvtest[y][(x-2)] = CAISSE_OK
                    return True
                else:
                    self.lvtest[y][(x-2)] = CAISSE
                    return True

        if pos == "droite":
            if self.lvtest[y][(x+2)] != MUR and self.lvtest[y][(x+2)] != CAISSE and self.lvtest[y][(x+2)] != CAISSE_OK:
                if self.lvtest[y][(x+1)] == CAISSE_OK:
                    self.lvtest[y][(x+1)] = OBJECTIF
                else:
                    self.lvtest[y][(x+1)] = VIDE
                if self.lvtest[y][(x+2)] == OBJECTIF:
                    self.lvtest[y][(x+2)] = CAISSE_OK
                    return True
                else:
                    self.lvtest[y][(x+2)] = CAISSE
                    return True

        if pos == "haut":
            if self.lvtest[(y-2)][x] != MUR and self.lvtest[(y-2)][x] != CAISSE and self.lvtest[(y-2)][x] != CAISSE_OK:
                if self.lvtest[(y-1)][x] == CAISSE_OK:
                    self.lvtest[(y-1)][x] = OBJECTIF
                else:
                    self.lvtest[(y-1)][x] = VIDE
                if self.lvtest[(y-2)][x] == OBJECTIF:
                    self.lvtest[(y-2)][x] = CAISSE_OK
                    return True
                else:
                    self.lvtest[(y-2)][x] = CAISSE
                    return True

        if pos == "bas":
            if self.lvtest[(y+2)][x] != MUR and self.lvtest[(y+2)][x] != CAISSE and self.lvtest[(y+2)][x] != CAISSE_OK:
                if self.lvtest[(y+1)][x] == CAISSE_OK:
                    self.lvtest[(y+1)][x] = OBJECTIF
                else:
                    self.lvtest[(y+1)][x] = VIDE
                if self.lvtest[(y+2)][x] == OBJECTIF:
                    self.lvtest[(y+2)][x] = CAISSE_OK
                    return True
                else:
                    self.lvtest[(y+2)][x] = CAISSE
                    return True

        return False

    def is_fini(self):
        lis = [self.lvtest[y/34][x/34] for (x, y) in self.coord_objec]
        return lis.count(5) == len(self.coord_objec)

if __name__ == '__main__' :
    g = Grille()
    g.genMap("lv1")
