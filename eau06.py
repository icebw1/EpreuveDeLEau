"""
Exercice : Majuscule sur deux
(slide 9)

Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.


Exemples d’utilisation :
$> python exo.py “Hello world !”
HeLlO wOrLd !


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.


"""
"""
Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.


Exemples d’utilisation :
$> python exo.py “Hello world !”
HeLlO wOrLd !


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.
"""

#Fonction
def majusculeSur2(t):
    i = 0                           #Indice qui parcourt le tableau
    y = 0                           #Indice qui gère l'espace pour mettre le caractere à la Maj/min

    while i < len(t):
        if t[i] == " ":
            print(end=" ")          #Afficher l'espace
            i = i + 1
            y = y + 2
        if y%2 == 0:
            print(end=t[i].upper()) #Afficher en majuscule
        elif y%2 != 0:  
            print(end=t[i].lower()) #Afficher en minuscule
        i = i + 1  
        y = y + 1   

#Parsing
x = input("Taper une phrase \n")

#Gestion d'erreur
if x.isdigit():
    print("Error") 
    exit()

#Affichage
majusculeSur2(x)

