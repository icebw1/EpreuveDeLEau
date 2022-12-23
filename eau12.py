"""
Exercice : Tri à bulle
(slide 15)

Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri à bulle.

Vous utiliserez une fonction de cette forme (selon votre langage) :
my_bubble_sort(array) 
{
	# votre algorithme
	return (new_array)
}


Exemples d’utilisation :
$> python exo.py 6 5 4 3 2 1
1 2 3 4 5 6


$> python exo.py test test test
error

Afficher error et quitter le programme en cas de problèmes d’arguments.


Wikipedia vous présentera une belle description de cet algorithme de tri.

"""
#Fonction

def triABulles(t):
    i = 0
    while i < len(t)-1: #à 1
            if t[i+1] < t[i]:
                (t[i+1], t[i]) = (t[i], t[i+1])
                i += 1

            elif t[i+1] > t[i]:
                (t[i+1], t[i]) = (t[i+1], t[i])
                i += 1           
    print(t)


try:
    #Parsing
    x = input("\n")
    tableau = x.split(" ")

    #Affichage
    triABulles(tableau)

#Gestion d'erreur
except ValueError:
    print("Erreur, la valeur entree est une chaine")
    exit()

"""
def triABulles(t):
    i = 0
    while i < len(t)-1: #à 1
        j = 0
        while j < i-1:
            if t[j+1] < t[j]:
                (t[j+1], t[j]) = (t[j], t[j+1])
                j += 1
            i += 1
    print(t)
"""