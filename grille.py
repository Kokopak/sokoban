#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from config import * 
import player

class Grille:
    def __init__(self, screen, fichier):
        self.screen = screen
        self.ref_img = {
            MUR: pygame.image.load("img/mur.jpg"),
            CAISSE: pygame.image.load("img/caisse.jpg"),
            OBJECTIF: pygame.image.load("img/objectif.png"),
            CAISSE_OK: pygame.image.load("img/caisse_ok.jpg"),
        }
        self.cases = {}
        self.objectifs = []
        self.player = player.Player()
        with open (fichier, 'r') as fich:
            for y, line in enumerate(fich) :
                for x, l in enumerate(line.strip().split(" ")) :
                    self.cases[x, y] = int(l)
                    if int(l) == OBJECTIF :
                        self.objectifs.append((x,y))
        self.lx = x+1
        self.ly = y+1

    def player_move(self, key):
        if key not in ( K_LEFT, K_RIGHT, K_UP,  K_DOWN) :
            return
        px, py = self.getPlayerPosition()
        self.player.set_position(key)
        fx, fy = self.case_move(px, py, key)

        if self.cases[fx, fy] in (CAISSE, CAISSE_OK) :
            cx, cy = self.case_move(fx, fy, key)
            if self.depl_ok(cx, cy) :
                if (fx, fy) in self.objectifs :
                    self.cases[fx, fy] = OBJECTIF
                else :
                    self.cases[fx, fy] = VIDE
                if (cx, cy) in self.objectifs :
                    self.cases[cx, cy] = CAISSE_OK
                else :
                    self.cases[cx, cy] = CAISSE
            else :
                return

        if self.depl_ok(fx, fy) :
            if (px, py) in self.objectifs :
                self.cases[px, py] = OBJECTIF
            else :
                self.cases[px, py] = VIDE
            self.cases[fx, fy] = PLAYER

        self.drawMap()


    def case_move(self, x, y, depl) :
        if depl == K_LEFT :
            pos = x-1, y
        elif depl == K_RIGHT :
            pos = x+1, y
        elif depl == K_UP :
            pos = x, y-1
        elif depl == K_DOWN :
            pos = x, y+1
        return pos

    def depl_ok(self, x, y) :
        if x<0 or x>=self.lx :
            return False
        if y<0 or y>=self.ly :
            return False
        return self.cases[x, y] not in (MUR, CAISSE, CAISSE_OK)

    def drawMap(self):
        for x in range(self.lx) :
            for y in range(self.ly) :
                c = self.cases[x, y]
                if c == PLAYER :
                    self.player.drawPlayer(self.screen, x, y)
                elif c == VIDE :
                    pass
                else:
                    self.screen.blit(self.ref_img[c], (x*SIZE, y*SIZE))
    
    def getPlayerPosition(self):
        for coord, case in self.cases.iteritems() :
            if case == PLAYER : 
                return coord

    def is_fini(self):
        lis = [self.cases[x, y] for (x, y) in self.objectifs]
        return lis.count(CAISSE_OK) == len(self.objectifs)

if __name__ == '__main__' :
    g = Grille()
    g.genMap("lv1")
