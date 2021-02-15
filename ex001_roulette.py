"""
Jeu sur la roulette (casino) qui comprend 13 chiffres allant de 0 à 12.
En plus des chiffres pairs et impairs, il y a certains chiffres qui sont noirs :
2,4,6,8,10,11 et certains chiffres sont rouges : 1,3,5,7,9,12 et le chiffre 0 n'a
pas de couleur
Le joueur donne un chiffre de 0 à 16
Pour les chiffres de 0 à 12 : il parie sur un chiffre avec une mise de 120
Pour les chiffres 13 et 14 : il parie sur pair / impairs avec une mise de 20
Pour les chiffres 15 et 16 : il parie sur la couleur rouge / la couleur noire avec une mise de 20
Sachant que le gain est de 0 si le joueur perd sa mise
"""

chiffre_joue = int(input())
chiffre_result = int(input())

if chiffre_joue < 13:
    if chiffre_result == chiffre_joue:
        print(120)
    else:
        print(0)
elif chiffre_joue == 13:
    if chiffre_result == 0 or chiffre_result == 2 or chiffre_result == 4 or chiffre_result == 6 or chiffre_result == 8 \
            or chiffre_result == 10 or chiffre_result == 12:
        print(20)
    else:
        print(0)
elif chiffre_joue == 14:
    if chiffre_result == 1 or chiffre_result == 3 or chiffre_result == 5 or chiffre_result == 7 or chiffre_result == 9 \
            or chiffre_result == 11:
        print(20)
    else:
        print(0)
elif chiffre_joue == 15:
    if chiffre_result == 1 or chiffre_result == 3 or chiffre_result == 5 or chiffre_result == 7 \
            or chiffre_result == 9 or chiffre_result == 12:
        print(20)
    else:
        print(0)
elif chiffre_joue == 16:
    if chiffre_result == 2 or chiffre_result == 4 or chiffre_result == 6 or chiffre_result == 8 or chiffre_result == 10\
            or chiffre_result == 11:
        print(20)
    else:
        print(0)
