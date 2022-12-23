"""
Exercice : Différence minimum absolue
(slide 14)

Créez un programme qui affiche la différence minimum absolue entre deux éléments d’un tableau constitué uniquement de nombres. Nombres négatifs acceptés.


Exemples d’utilisation :
$> python exo.py 5 1 19 21
2


$> python exo.py 20 5 1 19 21
1

$> python exo.py -8 -6 4
2

Afficher error et quitter le programme en cas de problèmes d’arguments.


"""
#Fonction
def minAbsolu(t):
    i = 0
    comparaison = float('inf')

    while i < len(t)-1:

        resultat = abs(int(t[i]) - int(t[i+1]))

        if resultat < comparaison:
            comparaison = resultat
        
        i = i + 1
    print(comparaison)


try:
    #Parsing
    x = input("\n")
    tableau = x.split(" ")

    #Affichage
    minAbsolu(tableau)

#Gestion d'erreur
except ValueError:
    print("Erreur, la valeur entree est une chaine")
    exit()

