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
        with open (fichier, 'r') as fich:
            for y, line in enumerate(fich) :
                for x, l in enumerate(line.strip().split(" ")) :
                    self.cases[x, y] = int(l)
                    if int(l) == OBJECTIF :
                        self.objectifs.append((x,y))
        self.lx = x+1
        self.ly = y+1
        self.player = player.Player()

    def player_move(self, key):
        # si mauvaise touche, on dégage
        if key not in ( K_LEFT, K_RIGHT, K_UP,  K_DOWN) :
            return

        # met le player dans la bonne direction
        self.player.set_position(key)
        # coord actuelles
        px, py = self.getPlayerPosition()
        # coord après déplacement
        fx, fy = self.case_move(px, py, key)

        # caisse à l'arrivée ?
        if self.depl_caisse_ok(fx, fy) and self.cases[fx, fy] in (CAISSE, CAISSE_OK) :
            cx, cy = self.case_move(fx, fy, key)
            # la caisse peut bouger
            if self.depl_ok(cx, cy) :
                # alors elle bouge
                self.vide(fx, fy)
                # vérifie si objectif atteint
                if (cx, cy) in self.objectifs :
                    self.cases[cx, cy] = CAISSE_OK
                else :
                    self.cases[cx, cy] = CAISSE
            # la caisse peut pas bouger, le player non plus
            # on sort
            else :
                return

        # le player peut bouger (y.c après le dépl de la caisse)
        if self.depl_ok(fx, fy) :
            self.vide(px, py)
            self.cases[fx, fy] = PLAYER

        # et on redessine
        self.drawMap()


    def vide(self, x, y) :
        # vide une case et remet à objectif s'il le faut
        if (x, y) in self.objectifs :
            self.cases[x, y] = OBJECTIF
            return True
        else :
            self.cases[x, y] = VIDE
            return False

    def case_move(self, x, y, depl) :
        # coord après depl
        if depl == K_LEFT :
            pos = x-1, y
        elif depl == K_RIGHT :
            pos = x+1, y
        elif depl == K_UP :
            pos = x, y-1
        elif depl == K_DOWN :
            pos = x, y+1
        return pos

    def depl_caisse_ok(self, x, y) :
        # vérif si dépl OK
        if x<0 or x>=self.lx :
            return False
        if y<0 or y>=self.ly :
            return False
        return self.cases[x, y] != MUR

    def depl_ok(self, x, y) :
        # vérif si dépl OK
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
        nb_obj = sum([self.cases[x, y]==CAISSE_OK for (x, y) in self.objectifs])
        return nb_obj == len(self.objectifs)

if __name__ == '__main__' :
    g = Grille()
    g.genMap("lv1")
