"""
Nombre de pliages d'une feuille d'une épaisseur de 0,0001 mètres pour accéder à la lune...
L'attribut DISTANCE (constante) est la distance en km entre la terre et la lune
"""

DISTANCE = 3.844e8
nombre_pliages: int = 0
epaisseur = 0.0001

while epaisseur < DISTANCE:
    nombre_pliages += 1
    epaisseur *= 2
print("Nombre de pliages nécessaires :", nombre_pliages)
