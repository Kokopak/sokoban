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
        self.coord_objec = []
        self.player = player.Player()
        with open (fichier, 'r') as fich:
            for x, line in enumerate(fich) :
                for y, l in enumerate(line.strip().split(" ")) :
                    self.cases[x, y] = int(l)
                    if int(l) == OBJECTIF :
                        self.coord_objec.append((x,y))
        self.lx = x+1
        self.ly = y+1

    def player_move(self, key):
        px, py = self.getPlayerPosition()
        if key == K_LEFT:
            self.player.set_position(GAUCHE)
            fx, fy = self.case_move(px, py, GAUCHE)
        elif key == K_RIGHT:
            self.player.set_position(DROITE)
            fx, fy = self.case_move(px, py, DROITE)
        elif key == K_UP:
            self.player.set_position(HAUT)
            fx, fy = self.case_move(px, py, HAUT)
        elif key == K_DOWN:
            self.player.set_position(BAS)
            fx, fy = self.case_move(px, py, BAS)
        if self.depl_ok(fx, fy) :
            if (px, py) in self.coord_objec :
                self.cases[px, py] = OBJECTIF
            else :
                self.cases[px, py] = VIDE
            self.cases[fx, fy] = PLAYER
            self.drawMap()

    def case_move(self, x, y, depl) :
        if depl == GAUCHE:
            pos = x-1, y
        elif depl == DROITE:
            pos = x+1, y
        elif depl == HAUT:
            pos = x, y-1
        elif depl == BAS:
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

    ##---Déplacement des caisses ---#
    #def moveCaisse(self, x, y, pos):
    #    self.is_fini()
    #    if pos == "gauche":
    #        if self.cases[y][x-2] not in (MUR, CAISSE, CAISSE_OK):
    #            if self.cases[y][x-1] == CAISSE_OK:
    #                self.cases[y][x-1] = OBJECTIF
    #            else:
    #                self.cases[y][x-1] = VIDE
    #            if self.cases[y][x-2] == OBJECTIF:
    #                self.cases[y][x-2] = CAISSE_OK
    #                return True
    #            else:
    #                self.cases[y][x-2] = CAISSE
    #                return True

    #    if pos == "droite":
    #        if self.cases[y][x+2] not in (MUR, CAISSE, CAISSE_OK):
    #            if self.cases[y][x+1] == CAISSE_OK:
    #                self.cases[y][x+1] = OBJECTIF
    #            else:
    #                self.cases[y][x+1] = VIDE
    #            if self.cases[y][x+2] == OBJECTIF:
    #                self.cases[y][x+2] = CAISSE_OK
    #                return True
    #            else:
    #                self.cases[y][x+2] = CAISSE
    #                return True

    #    if pos == "haut":
    #        if self.cases[y-2][x] not in (MUR, CAISSE, CAISSE_OK):
    #            if self.cases[y-1][x] == CAISSE_OK:
    #                self.cases[y-1][x] = OBJECTIF
    #            else:
    #                self.cases[y-1][x] = VIDE
    #            if self.cases[y-2][x] == OBJECTIF:
    #                self.cases[y-2][x] = CAISSE_OK
    #                return True
    #            else:
    #                self.cases[y-2][x] = CAISSE
    #                return True

    #    if pos == "bas":
    #        if self.cases[y+2][x] not in (MUR, CAISSE, CAISSE_OK):
    #            if self.cases[y+1][x] == CAISSE_OK:
    #                self.cases[y+1][x] = OBJECTIF
    #            else:
    #                self.cases[y+1][x] = VIDE
    #            if self.cases[y+2][x] == OBJECTIF:
    #                self.cases[y+2][x] = CAISSE_OK
    #                return True
    #            else:
    #                self.cases[y+2][x] = CAISSE
    #                return True
    #    return False

    #def checkCollision(self, pos):
    #    self.hauty = self.y - 1
    #    self.basy = self.y + 1
    #    self.droitex = self.x + 1
    #    self.gauchex = self.x - 1
    #    
    #    for y in range(len(self.grille.cases)):
    #        for x in range(len(self.grille.cases[y])):
    #            if self.position == self.gauche:
    #                pos_grille = self.grille.cases[self.y][self.gauchex]
    #                if pos_grille == CAISSE or pos_grille == CAISSE_OK:
    #                    a = self.grille.moveCaisse(self.x, self.y, "gauche")
    #                    if a:
    #                        self.x = self.gauchex
    #                return pos_grille == MUR or pos_grille == CAISSE or pos_grille == CAISSE_OK
    #            elif self.position == self.droite:
    #                pos_grille = self.grille.cases[self.y][self.droitex]
    #                if  pos_grille == CAISSE or pos_grille == CAISSE_OK:
    #                    a = self.grille.moveCaisse(self.x, self.y, "droite")
    #                    if a:
    #                        self.x = self.droitex
    #                return pos_grille == MUR or  pos_grille == CAISSE or pos_grille == CAISSE_OK
    #            elif self.position == self.haut:
    #                pos_grille = self.grille.cases[self.hauty][self.x]
    #                if  pos_grille == CAISSE or pos_grille == CAISSE_OK:
    #                    a = self.grille.moveCaisse(self.x, self.y, "haut")
    #                    if a:
    #                        self.y = self.hauty
    #                return pos_grille == MUR or  pos_grille == CAISSE or pos_grille == CAISSE_OK
    #            elif self.position == self.bas:
    #                pos_grille = self.grille.cases[self.basy][self.x]
    #                if  pos_grille == CAISSE or pos_grille == CAISSE_OK:
    #                    a = self.grille.moveCaisse(self.x, self.y, "bas")
    #                    if a:
    #                        self.y = self.basy
    #                return pos_grille == MUR or  pos_grille == CAISSE or pos_grille == CAISSE_OK
    def is_fini(self):
        lis = [self.cases[x, y] for (x, y) in self.coord_objec]
        return lis.count(CAISSE_OK) == len(self.coord_objec)

if __name__ == '__main__' :
    g = Grille()
    g.genMap("lv1")
