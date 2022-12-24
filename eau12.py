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
    j = 0   
    while i <= len(t)-j:     #Après le 1er parcous, le plus grand nb étant à sa position définitive (en dernier) : il n'a plus à être traité. 
            if i == len(t)-1:
                i = 0
                j = j + 1

            if int(t[i]) <= int(t[i+1]):
                print(str(t[i]) + " <= " + str(t[i+1]) + " à i = " + str(i))
                (t[i], t[i+1]) = (t[i], t[i+1])
                print(t)

            elif int(t[i]) > int(t[i+1]):
                print(str(t[i]) + " > " + str(t[i+1]) + " à i = " + str(i))
                (t[i], t[i+1]) = (t[i+1], t[i])
                print(t)

            i = i + 1
            print("i = i + 1")
            print("\n")


try:
    #Parsing
    x = input("Ce programme trie une liste de nombres (Tri à bulle).\n")
    tableau = x.split(" ")

    #Affichage
    triABulles(tableau)

#Gestion d'erreur
except ValueError:
    print("Erreur, la valeur entree est une chaine")
    exit()
