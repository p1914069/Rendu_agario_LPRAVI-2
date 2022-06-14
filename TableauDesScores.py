# ==================================================================================================================== #
# Ce fichier appartient au projet du cours d'informatique qui a lieu dans le cadre de la licence professionnelle       #
# RAVI | Promo 2021-2022. Ce projet a été réalisé en binôme par Arnaud MORMONT et Matéo ROLLET.                        #
# Nous contacter : arnaud.mormont@etu.univ-lyon1.fr | mateo.rollet@etu.univ-lyon1.fr                                   #
# ==================================================================================================================== #
# Fichier créé par : Arnaud MORMONT et Matéo ROLLET.                                                                   #
# Objectif de ce fichier: Contenir la classe du tableau des scores du jeu agar.io.                                     #
# ==================================================================================================================== #

import pygame


class TableauDesScores:
    """ Classe pour l'affichage des scores/compteurs du jeu agar.io. """
    def __init__(self):
        pygame.font.init()
        self.police = (pygame.font.SysFont('Segoe UI', 22))
        self.compteurEnnemis = 0
        self.compteurCreeps = 0

    def dessiner(self, screen, couleurFond):
        """ Méthode qui permet de dessiner le tableau. """
        pygame.draw.rect(screen, couleurFond, pygame.Rect(5, 5, 200, 100))
