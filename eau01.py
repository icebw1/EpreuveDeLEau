"""
Exercice : Combinaison de 2 nombres
(slide 4)

Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.


Exemples d’utilisation :
$> python exo.py
00 01, 00 02, 00 03, 00 04, ... , 00 99, 01 02, ... , 97 99, 98 99
$>

"""
#Fonction
for i in range(00, 100):
    for j in range(00, 100):
        if i < 10 and j < 10:
            print("0"+ str(i) + " " + "0" + str(j))
            continue

        elif i < 10 and j >= 10:
            print("0"+ str(i) + " " + str(j))
            continue

        elif i >= 10 and j < 10:
            print(str(i) + " " + "0" + str(j))
            continue

        if i == j:
            continue
        print(j, i)

