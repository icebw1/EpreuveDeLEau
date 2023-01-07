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
Le principe du tri par sélection est le suivant :
- rechercher le plus petit élément du tableau, et l'échanger avec l'élément d'indice 0 ;
- rechercher le second plus petit élément du tableau, et l'échanger avec l'élément d'indice 1 ;
- continuer de cette façon jusqu'à ce que le tableau soit entièrement trié.
"""
#Fonction

def triParSelection(t):
    i = 0
    j = 0
    k = 0
    longueurTableau = len(t)-1
    nouveauTableau = []
    
    while i <= longueurTableau and t[longueurTableau] != max(t):
        while j <= longueurTableau and t[j] != min(t):
            j = j + 1
        switcher = t[i]
        t[i] = t[j]
        t[j] = switcher 
        nouveauTableau.append(t[i])
        t[i] = float('inf')
        i = i + 1
        j = i

    print(end="\n")
    while k < longueurTableau:
        print(end=str(nouveauTableau[k]))
        print(end= " ")
        k = k + 1
    
try:
    #Parsing
    x = input("Ce programme trie une liste de nombres (Tri par sélection).\n")
    tableau = x.split(" ")
    int_tableau = list(map(int, tableau))   #Convertir tous les éléments du tableau en int

    #Affichage
    triParSelection(int_tableau)

#Gestion d'erreur
except ValueError:
    print("Erreur, la valeur entree est une chaine")
    exit()








"""
def triParSelection(t):
    i = 0
    j = 0
    longueurTableau = len(t)-1
    nouveauTableau = []
    
    while i <= longueurTableau and t[longueurTableau] != max(t):
        while j <= longueurTableau and t[j] != min(t):
            j = j + 1
        print("Le min est à l'index j = " + str(j) + ", t[j] = " + str(t[j]))
        print("t[i] = " + str(t[i]))
        print("i = " + str(i))
        print("j = " + str(j))
        switcher = t[i]
        t[i] = t[j]
        t[j] = switcher 
        nouveauTableau.append(t[i])
        print("Switch")
        print("Maintenant, t[j] = " + str(t[j]))
        print("t[i] = " + str(t[i]))
        print(t)
        t[i] = float('inf')
        i = i + 1
        j = i
        print("Après itération, i = " + str(i))
        print("Et j = " + str(j))
        print("min = " + str(min(t)))
        print("\n")

    print(nouveauTableau)
"""