"""
Exercice : Paramètres à l'envers
(slide 5)

Créez un programme qui affiche ses arguments reçus à l’envers.


Exemples d’utilisation :
$> python exo.py “Suis” “Je” “Drôle”
Drôle
Je
Suis


$> python exo.py ha ho
ho
ha

$> python exo.py “Bonjour 36”
Bonjour 36

Afficher error et quitter le programme en cas de problèmes d’arguments.
"""
#Fonction
def inverseChaine(t):

    i = len(t)-1  
    while i >= 0:
        print(end=t[i])
        print(end=" ")
        i = i - 1

#Parsing 
x = input("Taper une phrase ")
tableau = x.split(" ")

#Gestion d'erreur

#Resolution
inverseChaine(tableau)
