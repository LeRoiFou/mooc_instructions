"""
Écrire un programme qui additionne des valeurs naturelles lues sur entrée et affiche le résultat. La première
donnée lue ne fait pas partie des valeurs à sommer. Elle détermine si la liste contient un nombre déterminé à
l’avance de valeurs à lire ou non :
-> si cette valeur est un nombre positif ou nul, elle donne le nombre de valeurs
à lire et à sommer ;
-> si elle est négative, cela signifie qu’elle est suivie d’une liste de données à lire qui sera
terminée par le caractère "F" signifiant que la liste est terminée.
Éditeur : Laurent REYNAUD
Date : 19-07-2020
"""

saisie = int(input())
somme = 0

if saisie != -1:
    for i in range(saisie):
        saisie = int(input())
        somme += saisie
    print(somme)
else:
    while saisie != "F":
        saisie = (input())
        if saisie != "F":
            somme += int(saisie)
    print(somme)
