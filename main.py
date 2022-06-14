# ==================================================================================================================== #
# Ce fichier appartient au projet du cours d'informatique qui a lieu dans le cadre de la licence professionnelle       #
# RAVI | Promo 2021-2022. Ce projet a été réalisé en binôme par Arnaud MORMONT et Matéo ROLLET.                        #
# Nous contacter : arnaud.mormont@etu.univ-lyon1.fr | mateo.rollet@etu.univ-lyon1.fr                                   #
# ==================================================================================================================== #
# Fichier créé par : Arnaud MORMONT et Matéo ROLLET.                                                                   #
# Objectif de ce fichier: Fichier main à lancer pour voir le rendu final du projet.                                    #
# Version 0.9                                                                                                          #
# ==================================================================================================================== #

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

from chargement_agario import ChargementAgario
from MenuPyQt import MenuPyQt

# Déclaration compteur utilisé pour le chargement
compteur = 0


class Chargement(QMainWindow):
    """ Classe du chargement avant le lancement du menu principal d'agar.io. """

    def __init__(self):
        QMainWindow.__init__(self)
        self.chargement_anime = ChargementAgario()
        self.chargement_anime.setup(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # Retirer le cadre et le titre de la fenêtre.
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Rendre le fond de la fenêtre transparent/invisible.

        # DÉBUT Qtimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # Valeur du Qtimer en ms
        self.timer.start(35)

        # Afficher la fenêtre
        self.show()

    def progress(self):
        """Méthode qui permet d'animer la barre de chargement et d'afficher le menu principal à la fin du chargement."""

        global compteur

        # Affectation valeur de la barre de chargement
        self.chargement_anime.barre_chargement.setValue(compteur)

        # Fermer le chargement et faire apparaître le menu principal
        if compteur > 100:
            # Arrêter le timer
            self.timer.stop()

            # Ouvrir menu principal
            self.menu = MenuPyQt()
            self.menu.show()

            # Fermer la fenêtre de chargement
            self.close()

        # Incrémentation de la valeur du compteur → animation chargement
        compteur = compteur + 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = Chargement()
    sys.exit(app.exec_())
