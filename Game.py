#!/usr/bin/python
# -*- coding: utf-8 -*-

from Grid import*
from Player import*

# /////////////////////////////////////////////////////
#
# TP2 du module de Techniques de Développement LOGiciel
#
# Groupe 3
# TP réalisé par RIU Clément et SPITZ Anne
#
# Rendu le
#
# /////////////////////////////////////////////////////


class Game:
    def __init__(self, taille, joueur_1, joueur_2):
        """
        Constructeur.
        :param taille: Taille de la grille
        :param joueur_1: Nom du premier joueur
        :param joueur_2: Nom du deuxième joueur
        """
        self.joueur_courant = 1
        assert (type(taille) == int)
        self.tableau = Grid(taille)
        assert (type(joueur_1) == str and type(joueur_2) == str)
        self.liste_joueurs = [joueur_1, joueur_2]
