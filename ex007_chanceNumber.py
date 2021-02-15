"""
Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret) compris entre 0 et 100.
Ensuite, le joueur doit deviner ce nombre en utilisant le moins d’essais possible.
À chaque tour, le joueur est invité à proposer un nombre et le programme doit donner une réponse parmi les suivantes :
« Trop grand » : si le nombre secret est plus petit que la proposition et qu’on n’est pas au maximum d’essais
« Trop petit » : si le nombre secret est plus grand que la proposition et qu’on n’est pas au maximum d’essais
« Gagné en n essais ! » : si le nombre secret est trouvé
« Perdu ! Le secret était nombre » : si le joueur a utilisé six essais sans trouver le nombre secret.

Éditeur : Laurent REYNAUD
Date : 19-07-2020
"""

import random

joueur = ""
secret = random.randint(0, 100)
nbre_tours = 0

while joueur != secret and nbre_tours < 6:
    nbre_tours += 1
    joueur = int(input())
    if joueur < secret:
        print("Trop petit")
    else:
        print("Trop grand")
if joueur != secret:
    print("Perdu ! Le secret était", secret)
else:
    print("Gagné en", nbre_tours, "essais !")
