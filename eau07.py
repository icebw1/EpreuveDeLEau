"""
Exercice : Majuscule
(slide 10)

Créez un programme qui met en majuscule la première lettre de chaque mot d’une chaîne de caractères. Les autres lettres devront être en minuscules. Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.


Exemples d’utilisation :
$> python exo.py “bonjour mathilde, comment vas-tu ?!”
Bonjour Mathilde, Comment Vas-tu ?!


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.


"""
#Fonction
def majuscule(t):
    i = 0                           #Indice qui parcourt le tableau
    y = 0                           #Indice qui gère l'espace pour mettre le caractere à la Maj/min

    while i < len(t):
        if i == 0:
            print(end=t[i].upper())   

        elif i > 0:
            print(end=t[i])

        if t[i] == " ":
            print(end=t[i+1].upper()) 

        i = i + 1  
        y = y + 1
         

#Parsing
x = input("Taper une phrase \n")

#Gestion d'erreur
if x.isdigit():
    print("Error") 
    exit()

#Affichage
majuscule(x)