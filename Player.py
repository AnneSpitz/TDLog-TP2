#!/usr/bin/python
# -*- coding: utf-8 -*-

# /////////////////////////////////////////////////////
#
# TP1 du module de Techniques de Développement LOGiciel
#
# Groupe 3
# TP réalisé par RIU Clément et SPITZ Anne
#
# Rendu le Jeudi 06 Octobre 2016
#
# /////////////////////////////////////////////////////


class Player:
    def __init__(self, nom):
        """

        :param nom:
        """
        self._score = 0
        self._nom = nom

    def get_nom(self):
        """

        :return:
        """
        return self._nom

    def get_score(self):
        """

        :return:
        """
        return self._score

    def augmente_score(self, valeur):
        """

        :param valeur:
        :return:
        """
        self._score += valeur

    def affiche_joueur(self, max_taille_nom):
        """
        Affiche les noms des joueurs et leurs scores.
        :return: Rien
        """
        print("{0: <{width}} : {1}".format(self.get_nom(), self.get_score(), width=max_taille_nom - len(self.get_nom())))