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

#Fonctions
for i in range(10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(0, 10):
            if j == k or i == k:
                continue
            print(i, j, k)







"""
def combinaison():
    for n in t3:
        print(end=str(n))
   

#Gestion d'erreurs

#Parsing <=> Stockage entrée utilisateur

#Resolution <=> Utilisation de la fonction

#Affichage
combinaison()
""" 