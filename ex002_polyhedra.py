"""
L'utilisateur choisit l'un des 5 polyèdres suivants en saisissant sa 1ère lettre
ainsi que la longueur son arrête (a)
(T)étraèdre dont le volume est ((2**(1/2))/12)*(a**3)
(C)ube dont le volume est a**3
(O)ctaèdre dont le volume est ((2**(1/2))/3)*(a**3)
(D)odécaèdre dont le volume est ((15+7*(5**(1/2)))/4)*(a**3)
(I)cosaèdre dont le volume est ((5*(3+5**(1/2))/12)*(a**3)
Si la lettre lue ne fait pas partie des 5 initiales, le programme imprime
le message "Polyèdre non connu"
"""

polyedre = input()
a = float(input())
if polyedre == "T":
    print(((2**(1/2))/12)*(a**3))
elif polyedre == "C":
    print(a**3)
elif polyedre == "O":
    print(((2**(1/2))/3)*(a**3))
elif polyedre == "D":
    print(((15+7*(5**(1/2)))/4)*(a**3))
elif polyedre == "I":
    print(((5*(3+5**(1/2))/12)*(a**3)))
else:
    print("Polyèdre non connu")
