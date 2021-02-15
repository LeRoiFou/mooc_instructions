"""
L'instruction répétitive 'for'
Cette boucle est équivalente à la boucle 'for each' dans Java
"""

for c in "Bonjour":
    print(c)

# Cette instruction donne les valeurs entières à partir de 0 jusqu'à 4 (le chiffre entier 5 est exclu)
for i in range(5):
    print(i)

# Cette instruction permet d'additionner les suites allant de 0 à 4
somme = 0
for i in range(5):
    somme += i
print(somme)
