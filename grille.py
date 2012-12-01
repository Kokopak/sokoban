#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame

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

    def genMap(self):
        self.lvtest = [ 
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                ]

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
        if pos == "gauche":
            if self.lvtest[y/34][(x-68)/34] != 1 and self.lvtest[y/34][(x-68)/34] != 2:
                self.lvtest[y/34][(x-34)/34] = 0
                if not self.valide_caisse:
                    if self.lvtest[y/34][(x-68)/34] == 3:
                        self.lvtest[y/34][(x-68)/34] = 5
                        self.valide_caisse = True
                    else:
                        self.lvtest[y/34][(x-68)/34] = 2
                else:
                    self.lvtest[y/34][(x-34)/34] = 3
                    self.lvtest[y/34][(x-68)/34] = 2
                    self.valide_caisse = False
        elif pos == "droite":
            if self.lvtest[y/34][(x+68)/34] != 1 and self.lvtest[y/34][(x+68)/34] != 2:
                self.lvtest[y/34][(x+34)/34] = 0
                if not self.valide_caisse:
                    if self.lvtest[y/34][(x+68)/34] == 3:
                        self.lvtest[y/34][(x+68)/34] = 5
                        self.valide_caisse = True
                    else:
                        self.lvtest[y/34][(x+68)/34] = 2
                else:
                    self.lvtest[y/34][(x+34)/34] = 3
                    self.lvtest[y/34][(x+68)/34] = 2
                    self.valide_caisse = False
        elif pos == "haut":
            if self.lvtest[(y-68)/34][x/34] != 1 and self.lvtest[(y-68)/34][x/34] != 2:
                self.lvtest[(y-34)/34][x/34] = 0
                if not self.valide_caisse:
                    if self.lvtest[(y-68)/34][x/34] == 3:
                        self.lvtest[(y-68)/34][x/34] = 5
                        self.valide_caisse = True
                    else:
                        self.lvtest[(y-68)/34][x/34] = 2
                else:
                    self.lvtest[(y-34)/34][x/34] = 3
                    self.lvtest[(y-68)/34][x/34] = 2
                    self.valide_caisse = False
        elif pos == "bas":
            if self.lvtest[(y+68)/34][x/34] != 1 and self.lvtest[(y+68)/34][x/34] != 2:
                self.lvtest[(y+34)/34][x/34] = 0
                if not self.valide_caisse:
                    if self.lvtest[(y+68)/34][x/34] == 3:
                        self.lvtest[(y+68)/34][x/34] = 5
                        self.valide_caisse = True
                    else:
                        self.lvtest[(y+68)/34][x/34] = 2
                else:
                    self.lvtest[(y+34)/34][x/34] = 3
                    self.lvtest[(y+68)/34][x/34] = 2
                    self.valide_caisse = False
        
