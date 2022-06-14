# ==================================================================================================================== #
# Ce fichier appartient au projet du cours d'informatique qui a lieu dans le cadre de la licence professionnelle       #
# RAVI | Promo 2021-2022. Ce projet a été réalisé en binôme par Arnaud MORMONT et Matéo ROLLET.                        #
# Nous contacter : arnaud.mormont@etu.univ-lyon1.fr | mateo.rollet@etu.univ-lyon1.fr                                   #
# ==================================================================================================================== #
# Fichier créé par : Arnaud MORMONT et Matéo ROLLET.                                                                   #
# Objectif de ce fichier: Créer un chargement fictif qui précèdera l'ouverture du menu principal du menu d'agar.io     #
# ==================================================================================================================== #


from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRect, QMetaObject
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtWidgets import QLabel, QFrame, QProgressBar, QWidget

from feuillestyle import FeuilleDeStyle


class ChargementAgario(object):
    """ Classe de défninition du chargement d'agar.io. """

    def setup(self, Chargement):
        """ Méthode permettant le setup du chargement d'agar.io. """
        Chargement.resize(340, 220)

        self.fenetre = QWidget(Chargement)

        # Suppression du titre de la fenêtre et fond de la fenêtre transparent
        Chargement.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Chargement.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Construction de la fenêtre de chargement
        self._init_fond()
        self._init_titre()
        self._init_barre_chargement()
        self._init_texte_chargement()

        Chargement.setCentralWidget(self.fenetre)

        QMetaObject.connectSlotsByName(Chargement)

    def _init_fond(self):
        self.fond = QFrame(self.fenetre)
        self.fond.resize(340, 220)
        self.fond.setObjectName('chargement_fond')

        self.fond.setCursor(QCursor(Qt.BusyCursor))
        self.fond.setStyleSheet(FeuilleDeStyle.feuille_style)

    def _init_titre(self):
        self.titre = QLabel(self.fond)
        self.titre.setObjectName('chargement_titre')
        self.titre.setGeometry(QRect(10, 10, 320, 110))

        self.police_titre = QFont()
        self.police_titre.setFamily("Segoe UI")
        self.police_titre.setPointSize(50)
        self.titre.setFont(self.police_titre)

        self.titre.setStyleSheet(FeuilleDeStyle.feuille_style)
        self.titre.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.titre.setText("<strong>Agar</strong>.io")

    def _init_barre_chargement(self):
        self.barre_chargement = QProgressBar(self.fond)
        self.barre_chargement.setObjectName('barre_chargement')

        self.barre_chargement.setGeometry(QRect(30, 135, 280, 23))
        self.barre_chargement.setStyleSheet(FeuilleDeStyle.feuille_style)

        self.barre_chargement.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.barre_chargement.setValue(0)

    def _init_texte_chargement(self):
        self.texte_chargement = QLabel(self.fond)
        self.texte_chargement.setObjectName('texte_chargement')
        self.texte_chargement.setGeometry(QRect(10, 160, 320, 30))

        self.police_texte_chargement = QFont()
        self.police_texte_chargement.setFamily("Segoe UI")
        self.police_texte_chargement.setPointSize(11)

        self.texte_chargement.setFont(self.police_texte_chargement)
        self.texte_chargement.setStyleSheet(FeuilleDeStyle.feuille_style)

        self.texte_chargement.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.texte_chargement.setText("chargement...")
