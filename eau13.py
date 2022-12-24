"""
Exercice : Tri par sélection
(slide 16)

Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri par sélection.

Vous utiliserez une fonction de cette forme (selon votre langage) :
my_select_sort(array) {
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

def triParSelection(t):
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
    triParSelection(tableau)

#Gestion d'erreur
except ValueError:
    print("Erreur, la valeur entree est une chaine")
    exit()
