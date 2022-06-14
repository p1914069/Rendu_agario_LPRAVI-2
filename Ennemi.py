# ==================================================================================================================== #
# Ce fichier appartient au projet du cours d'informatique qui a lieu dans le cadre de la licence professionnelle       #
# RAVI | Promo 2021-2022. Ce projet a été réalisé en binôme par Arnaud MORMONT et Matéo ROLLET.                        #
# Nous contacter : arnaud.mormont@etu.univ-lyon1.fr | mateo.rollet@etu.univ-lyon1.fr                                   #
# ==================================================================================================================== #
# Fichier créé par : Arnaud MORMONT et Matéo ROLLET.                                                                   #
# Objectif de ce fichier: Contenir la classe des ennemis du jeu agar.io.                                                #
# ==================================================================================================================== #

import random
import pygame
from pygame import Vector2

import core


class Ennemi:
    """ Classe pour les ennemis du jeu agar.io. """

    def __init__(self):
        self.rayon = 5
        self.rayon_max = 150
        self.couleur = (random.randint(40, 240), 0, 0)
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))
        self.nom = "ENNEMI"
        self.uuid = random.randint(1000000000, 999999999999)

        self.direction = Vector2(0, 0)
        self.raideur = 0.00025
        self.vitesse = 1
        self.vitessemax = 2
        self.Fx = 0
        self.Ux = Vector2(0, 0)
        self.l = 0
        self.l0 = 1
        self.L = 0

        self.ChampVisionEnnemi = 2000
        self.ChampVisionEnnemi_resultat = 0

        self.nouvelle_liste = []

    def mourir(self):
        """ Méthode qui permet de repositionner les ennemis. → Faire comme s'ils mourraient. """
        self.rayon = 5
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))

    def draw(self, screen):
        """ Méthode qui permet de dessiner les ennemis. """
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)
        core.Draw.circle(self.couleur, self.position, self.ChampVisionEnnemi, 1)
        core.Draw.line((255,0,0),self.position, self.position+self.direction*50,2)

    def perception(self, liste_creeps, liste_ennemis, joueur):
        """ [PAS FONCTIONNEL] Méthode qui permet aux ennemis d'avoir un champ de vision circulaire. """
        self.liste_creeps = liste_creeps
        self.liste_ennemis = liste_ennemis
        self.joueur_detec = joueur
        self.liste_percu_e = []
        self.liste_percu_c = []
        self.joueur_vu = 0

        # print(self.liste_creeps, self.liste_ennemis, self.joueur_detec)
        for ennemi in self.liste_ennemis:
            if self.ChampVisionEnnemi > self.position.distance_to(ennemi.position) and self != ennemi:
                self.liste_percu_e.append(ennemi)

        for creep in self.liste_creeps:
            if self.ChampVisionEnnemi > self.position.distance_to(creep.position):
                self.liste_percu_c.append(creep)

        if self.ChampVisionEnnemi > self.position.distance_to(self.joueur_detec.position):
            self.joueur_vu = 1
        else:
            self.joueur_vu = 0

        # for i in self.liste_percu:
        #     print(i.uuid)

    def grossir(self):
        """ Méthode qui permet aux ennemis de grossir. """
        if self.rayon < self.rayon_max:
            self.rayon = self.rayon + 1
            self.ChampVisionEnnemi = self.ChampVisionEnnemi + 6

            self.vitessemax = self.vitessemax * 0.988
            self.Fx = self.vitesse * self.Fx

    def deplacement_aleatoire(self, h, l):
        """ Méthode qui permet aux ennemis de se déplacer aléatoirement. """
        self.Fx = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

        self.direction = self.direction + self.Fx

        if self.direction.length() > self.vitessemax and self.direction.length() != 0:
            self.direction.normalize()
            self.direction.scale_to_length(self.vitessemax)

        self.position = self.direction + self.position

        if self.position.y < 0 or self.position.y > h:
            self.direction = Vector2(0, self.direction.y * -1)

        if self.position.x < 0 or self.position.x > l:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)

    def fuite(self, h, l, j, detection):

        if self.position.y < 0 or self.position.y > h:
            self.direction = Vector2(0, self.direction.y * -1)

        if self.position.x < 0 or self.position.x > l:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)

        if detection is not None:

            self.Ux = j - self.position
            self.l = self.Ux.length()
            self.Ux = self.Ux.normalize()
            self.L = abs(self.l - self.l0)

            self.Fx = self.raideur * self.L * self.Ux
            self.direction = self.direction + self.Fx

        else:
            self.Ux = Vector2(0, 0)

        if self.direction.length() > self.vitessemax and self.direction.length() != 0:
            self.direction.normalize()
            self.direction.scale_to_length(self.vitessemax)

        self.position = self.direction + self.position

    def deplacement_versCreep(self, h, l):
        """ [PAS FONCTIONNEL] Méthode qui permet aux ennemis de trouver et de se déplacer vers les creeps présents
        dans leur champ de vision. """
        # self.Fx = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

        self.liste_percu_c.sort(key=lambda x: x.position.distance_to(self.position), reverse=True)

        self.nouvelle_liste = sorted(self.liste_percu_c, key=lambda x: x.position.distance_to(self.position), reverse=True)

        if len(self.nouvelle_liste) > 0:
            creep = self.nouvelle_liste[0]
            self.Ux = creep.position - self.position
            self.l = self.Ux.length()
            self.Ux = self.Ux.normalize()
            self.L = abs(self.l - self.l0)

            self.Fx = self.raideur * self.L * self.Ux
            self.direction = self.direction + self.Fx

            self.Ux = Vector2(0, 0)

            if self.direction.length() > self.vitessemax and self.direction.length() != 0:
                self.direction.normalize()
                self.direction.scale_to_length(self.vitessemax)

            self.position = self.direction + self.position

            if self.position.y < 0 or self.position.y > h:
                self.direction = Vector2(0, self.direction.y * -1)

            if self.position.x < 0 or self.position.x > l:
                self.direction = Vector2(self.direction.x * -1, self.direction.y)
