"""
Exercice : Combinaison de 3 chiffres
(slide 3)

Créez un programme qui affiche toutes les différentes combinaisons possibles de trois chiffres dans l’ordre croissant, dans l’ordre croissant. La répétition est volontaire.

Exemples d’utilisation :
$> python exo.py
012, 013, 014, 015, 016, 017, 018, 019, 023, 024, ... , 789
$>

987 n’est pas là parce que 789 est présent.

020 n’est pas là parce que 0 apparaît deux fois.

021 n’est pas là parce que 012 est présent.

000 n’est pas là parce que cette combinaison ne comporte pas exclusivement des chiffres différents les uns des autres.
"""
tableau = []
"""
#Fonctions
for i in range(10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(0, 10):
            if j == k or i == k:
                continue
            elif i == 9 and j == 8 and k == 7:
                print(i, j, k, end=".")
                continue

            print(i, j, k, end=", ")
"""         
           

#Fonctions
for i in range(10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(0, 10):
            if j == k or i == k:
                continue

            if nombre = str(i) + str(k) + str(j) or nombre = str(j) + str(i) + str(k) or nombre = str(j) + str(k) + str(i) or nombre = str(k) + str(i) + str(j) or nombre = str(k) + str(j) + str(i):
                continue

            elif i == 9 and j == 8 and k == 7:
                print(i, j, k, end=".")
                continue

            print(i, j, k, end=", ")
            #nombre = str(i) + str(j) + str(k)
            #tableau.append(nombre)

             #print(tableau)
