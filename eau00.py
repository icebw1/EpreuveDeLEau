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
"""
compteurA = 0
compteurB = 1
compteurC = 2
i = 0

while i < 30:

    a = compteurA
    b = compteurB
    c = compteurC
    
    if a == b:
        b = compteurB + 1

        if a == c:
            c = compteurC + 1

            if b == c:
                c = compteurC + 2
            

    if compteurC == 10:

        compteurC = b + 2
        b = compteurB + 1
        c = compteurC

    print(end=str(a) +str(b) + str(c))
    print(end=", ")

    compteurC = compteurC + 1
    
    i = i + 1
 


"""
t1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
t2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
t3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 1

while i < 100:

    x = 0
    y = 1
    z = 2

    while y < len(t2)-1:

        while z < len(t3)-1:
            print(end= str(t1[x]) + str(t2[y]) + str(t3[z]))
            print(end=", ")

            z = z + 1


        print(end= str(t1[x]) + str(t2[y]) + str(t3[z]))
        print(end=", ")

        y = y + 1
        z = y + 1








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