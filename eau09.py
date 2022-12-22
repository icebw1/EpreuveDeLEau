"""
Exercice : Entre min et max
(slide 12)

Créez un programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. Min inclus, max exclus.

Exemples d’utilisation :
$> python exo.py 20 25
20 21 22 23 24


$> python exo.py 25 20
20 21 22 23 24

$> python exo.py hello
error

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""
#Fonction
def entreMinEtMax(a, b):
    #i = 0
    if a < b:
        print(end=str(a) + " ")  
        while a < b-1:
            a = a + 1
            print(end=str(a) + " ")  

    elif a > b:
        print(end=str(b) + " ")  
        while a-1 > b:
            b = b + 1
            print(end=str(b) + " ")  

#Parsing
x = input("\n")
tableau = x.split(" ")

nInt1 = int(tableau[0])
nInt2 = int(tableau[1])

#Gestion d'erreur
if not x.isdigit():
    print("error") 
    exit()

#Affichage
entreMinEtMax(nInt1, nInt2)
