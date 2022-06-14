# ==================================================================================================================== #
# Ce fichier appartient au projet du cours d'informatique qui a lieu dans le cadre de la licence professionnelle       #
# RAVI | Promo 2021-2022. Ce projet a été réalisé en binôme par Arnaud MORMONT et Matéo ROLLET.                        #
# Nous contacter : arnaud.mormont@etu.univ-lyon1.fr | mateo.rollet@etu.univ-lyon1.fr                                   #
# ==================================================================================================================== #
# Fichier créé par : Arnaud MORMONT et Matéo ROLLET.                                                                   #
# Objectif de ce fichier: Contenir la classe des creeps du jeu agar.io.                                                #
# ==================================================================================================================== #

import random
import pygame
from pygame import Vector2


class Creep:
    """ Classe pour les creeps du jeu agar.io. """
    def __init__(self):
        self.rayon = 2
        self.couleur = (random.randint(20, 215), random.randint(20, 215), random.randint(20, 215))
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))

    def mourir(self):
        """ Méthode qui permet de repositionner les creeps. → Faire comme s'ils mourraient. """
        self.couleur = (random.randint(20, 215), random.randint(20, 215), random.randint(20, 215))
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))

    def draw(self, screen):
        """ Méthode pour dessiner les creeps. """
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)
