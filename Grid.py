#!/usr/bin/python
# -*- coding: utf-8 -*-

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


class Grid:
    def __init__(self, taille):
        """
        Constructeur.
        :param taille:
        """
        assert (taille % 2 == 1)
        self._tableau = [[None for i in range(taille)] for i in range(taille)]

    def get_taille(self):
        """
        Assesseur en lecture de la taille de la grille.
        :return: Un int correspondant à la taille de la Grid.
        """
        return len(self._tableau)

    def get_cellule(self, x, y):
        """
        Assesseur en lecture de la cellule de coordonnées (x, y)
        :param x: Coordonnée en abscisse.
        :param y: Coordonnée en ordonnée.
        :return: la valeur de la cellule.
        """
        assert (x, y) in self
        return self._tableau[x][y]

    def set_cellule(self, valeur, x, y):
        """
        Assesseur en écriture de la cellule de coordonnées (x, y)
        :param valeur: valeur à mettre en (x, y)
        :param x: Coordonnée en abscisse.
        :param y: Coordonnée en ordonnée.
        :return: Rien.
        """
        self._tableau = valeur

    def __contains__(self, (x, y)):
        """
        :param x: Coordonnée en abscisse.
        :param y: Coordonnée en ordonnée.
        :return: True si les coordonnées x et y sont valides. False sinon.
        """
        taille = self.get_taille()
        return x * y >= 0 and x * y < taille ** 2

