"""
Écrire un programme qui lit en entrée une valeur naturelle n et qui affiche à l’écran un triangle supérieur droit
formé de X

Éditeur : Laurent REYNAUD
Date : 19-07-2020
"""

nbrecroix = int(input())
ligne = "X" * nbrecroix
espaces = 0
print(ligne)

for i in ligne:
    if nbrecroix > 1:
        nbrecroix -= 1
        espaces += 1
        ligne = "X" * nbrecroix
        print(" " * espaces + ligne)
