#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import yaml

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
        #f = open("lv1.yaml", "w");
        with open (fichier, 'rb') as fich:
            self.lvtest = yaml.load(fich)
        #    self.lvtest = [[int(l) for l in line.strip().split(" ")] for line in fich]
        #    yaml.dump(self.lvtest, f)

        #self.lvtest = [ 
        #        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        #        [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #        [1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1],
        #        [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
        #        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #        [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
        #        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #        [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1],
        #        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        #        ]
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
            if self.lvtest[y/34][(x-68)/34] != 1 and self.lvtest[y/34][(x-68)/34] != 2 and self.lvtest[y/34][(x-68)/34] != 5:
                if self.lvtest[y/34][(x-34)/34] == 5:
                    self.lvtest[y/34][(x-34)/34] = 3
                else:
                    self.lvtest[y/34][(x-34)/34] = 0
                if self.lvtest[y/34][(x-68)/34] == 3:
                    self.lvtest[y/34][(x-68)/34] = 5
                    return True
                else:
                    self.lvtest[y/34][(x-68)/34] = 2
                    return True

        if pos == "droite":
            if self.lvtest[y/34][(x+68)/34] != 1 and self.lvtest[y/34][(x+68)/34] != 2 and self.lvtest[y/34][(x+68)/34] != 5:
                if self.lvtest[y/34][(x+34)/34] == 5:
                    self.lvtest[y/34][(x+34)/34] = 3
                else:
                    self.lvtest[y/34][(x+34)/34] = 0
                if self.lvtest[y/34][(x+68)/34] == 3:
                    self.lvtest[y/34][(x+68)/34] = 5
                    return True
                else:
                    self.lvtest[y/34][(x+68)/34] = 2
                    return True

        if pos == "haut":
            if self.lvtest[(y-68)/34][x/34] != 1 and self.lvtest[(y-68)/34][x/34] != 2 and self.lvtest[(y-68)/34][x/34] != 5:
                if self.lvtest[(y-34)/34][x/34] == 5:
                    self.lvtest[(y-34)/34][x/34] = 3
                else:
                    self.lvtest[(y-34)/34][x/34] = 0
                if self.lvtest[(y-68)/34][x/34] == 3:
                    self.lvtest[(y-68)/34][x/34] = 5
                    return True
                else:
                    self.lvtest[(y-68)/34][x/34] = 2
                    return True

        if pos == "bas":
            if self.lvtest[(y+68)/34][x/34] != 1 and self.lvtest[(y+68)/34][x/34] != 2 and self.lvtest[(y+68)/34][x/34] != 5:
                if self.lvtest[(y+34)/34][x/34] == 5:
                    self.lvtest[(y+34)/34][x/34] = 3
                else:
                    self.lvtest[(y+34)/34][x/34] = 0
                if self.lvtest[(y+68)/34][x/34] == 3:
                    self.lvtest[(y+68)/34][x/34] = 5
                    return True
                else:
                    self.lvtest[(y+68)/34][x/34] = 2
                    return True

        return False

    def is_fini(self):
        lis = [self.lvtest[y/34][x/34] for (x, y) in self.coord_objec]
        return lis.count(5) == len(self.coord_objec)

if __name__ == '__main__' :
    g = Grille()
    g.genMap("lv1")
