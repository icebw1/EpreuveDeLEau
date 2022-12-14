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
def inverseChaine(t):
    
    i = len(t)-1  
    while i >= 0:
        print(end=tableau[i])
        print(end=" ")
        i = i - 1


