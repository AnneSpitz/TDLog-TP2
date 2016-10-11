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


from Grid import *
from player import *
from random import choice

direction_acceptable = {"8": [0, -1], "4": [-1, 0], "2": [0, 1], "6": [1, 0], "7": [-1, -1], "9": [1, -1], "1": [-1, 1],
                        "3": [1, 1]}


def add(x, y):
    """
    Permet d'additionner terme à terme deux couples ou deux tableaux
    :param x:
    :param y:
    :return: le résultat, sous forme de tableau
    """
    assert (len(x) == len(y))
    return [x[i] + y[i] for i in range(len(x))]


class Game:
    def __init__(self, taille, joueur_1, joueur_2):
        """
        Constructeur.
        :param taille: Taille de la grille
        :param joueur_1: Nom du premier joueur
        :param joueur_2: Nom du deuxième joueur
        """
        self.joueur_courant = 0

        assert (type(taille) == int)
        self.tableau = Grid(taille)
        for x in range(taille):
            for y in range(taille):
                self.tableau.set_cellule(choice(point), (x, y))

        assert (type(joueur_1) == str and type(joueur_2) == str)
        self.liste_joueurs = [Player(joueur_1), Player(joueur_2)]

        assert (taille % 2 == 1)
        self.positions = [taille // 2, taille // 2]

    def demande_direction(self):
        """
        Demande à l'utilisateur de rentrer une touche du clavier.
        :return: une string correspondant à la touche demandée.
        """
        return raw_input(
            "À {0} de jouer. \n Appuyer sur une touche parmi : {1}; {2}; {3}; {4}; {5}; {6}; {7}; {8}. Choisissez une case non vide.".format(
                self.liste_joueurs[self.joueur_courant].get_nom(), *direction_acceptable.keys()))

    def test_direction(self, direction):
        """

        :return:
        """
        position_voulue = add(self.positions, direction_acceptable[direction])
        if direction not in direction_acceptable.keys():
            return True
        elif position_voulue not in self.tableau:
            return True
        elif type(self.tableau.get_cellule(position_voulue)) == int:
            return True
        else:
            return False

    def gestion_tour(self):
        """
        Permet de jouer pour le joueur courant, puis passe la main.
        :param direction: direction dans laquel le joueur veut se déplacer.
        :return: Rien
        """
        direction = self.demande_direction()
        while direction not in direction_acceptable.keys() or (
                (add(self.positions, direction_acceptable[direction])) in self.tableau and not type(
                self.tableau.get_cellule(add(self.positions, direction_acceptable[direction]))) == int) or (
            (add(self.positions, direction_acceptable[direction])) not in self.tableau):
            direction = self.demande_direction()

        self.positions = add(self.positions, direction_acceptable[direction])
        self.liste_joueurs[self.joueur_courant].augmente_score(self.tableau.get_cellule(self.positions))
        self.tableau.set_cellule(None, self.positions)
        self.joueur_courant = (self.joueur_courant + 1) % 2

        return None

    def fin_partie(self):
        """
        Permet de déterminer si la partie est finie ou non, c'est à dire, s'il reste des directions acceptable avec des points à marquer.
        :return: True si la partie est finie, False sinon.
        """
        for direction in direction_acceptable.values():
            position_testee = add(self.positions, direction)
            if position_testee in self.tableau and type(self.tableau.get_cellule(position_testee)) == int:
                return False
        return True

    def resultat_partie(self):
        """
        Affiche le résultat de la partie et renvoie le numéro du joueur vainqueur.
        :return: 1 ou 2 selon le joueur qui a gagné, None sinon.
        """
        score_joueur_1 = self.liste_joueurs[0].get_score()
        score_joueur_2 = self.liste_joueurs[1].get_score()
        if score_joueur_1 > score_joueur_2:
            print("Le joueur 1 a gagné ! Son score est de {} points contre {}".format(str(score_joueur_1),
                                                                                      str(score_joueur_2)))
            return 1
        elif score_joueur_1 == score_joueur_2:
            print("Il y a une égalité ! Les deux joueurs ont {} points".format(str(score_joueur_2)))
            return None
        else:
            print("Le joueur 2 a gagné ! Son score est de {} points contre {}".format(str(score_joueur_2),
                                                                                      str(score_joueur_1)))
            return 2

    def affichage(self):
        """
        Affiche l'état actuelle de la partie.
        :return: Rien
        """
        self.tableau.affichage_grille(self.positions)
        max_length = max(len(self.liste_joueurs[i].get_nom()) for i in {0, 1})
        self.liste_joueurs[0].affiche_joueur(max_length)
        self.liste_joueurs[1].affiche_joueur(max_length)
        print("\n")


def gestion_jeu():
    """
    Fonction permettant le jeu.
    :return: Le numéro du joueur gagnant.
    """
    taille = input("Bienvenue ! Choisissez la taille de la grille. \n")
    if taille % 2 == 0:
        taille += 1
    nom_joueur_1 = raw_input("Joueur 1 : quel est votre nom ? \n")
    nom_joueur_2 = raw_input("Joueur 2 : quel est votre nom ? \n")

    partie = Game(taille, nom_joueur_1, nom_joueur_2)
    partie.affichage()
    while not partie.fin_partie():
        partie.gestion_tour()
        partie.affichage()
    return partie.resultat_partie()


gestion_jeu()
