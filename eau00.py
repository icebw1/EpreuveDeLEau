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
#Fonction
tableau = []

for i in range(10):
    for j in range(1, 10):
        if str(i) == str(j):
            continue
        for k in range(0, 10):
            if str(j) == str(k) or str(i) == str(k):
                continue

            elif (str(i) + str(k) + str(j)) in tableau or (str(k) + str(i) + str(j)) in tableau or (str(k) + str(j) + str(i)) in tableau or (str(j) + str(i) + str(k)) in tableau or (str(j) + str(k) + str(i)) in tableau:
                continue

            tableau.append(str(i) + str(j) + str(k))

for n in tableau:
    if str(n) == "789":
        print(end=n + ".")
        exit()
    print(end=n + ", ")
