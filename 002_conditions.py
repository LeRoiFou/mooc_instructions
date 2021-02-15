"""
Petit jeu de devinette version 1 :
tirage aléatoire entre 0 et 5 et demande à l'utilisateur de trouver le nombre

Auteur : laurent REYNAUD
Date : 16-07-2020
"""

import random

secret = random.randint(0, 5)
revelation = int(input("Veuillez saisir un chiffre entre 0 et 5 please : "))
if revelation == secret:
    print("gagné !")
else:
    print("perdu ! La valeur était", secret)
