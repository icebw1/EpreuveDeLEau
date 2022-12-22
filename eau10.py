"""
Exercice : Index wanted
(slide 13)

Créez un programme qui affiche le premier index d’un élément recherché dans un tableau. Le tableau est constitué de 
tous les arguments sauf le dernier. 
L’élément recherché est le dernier argument. Afficher -1 si l’élément n’est pas trouvé.

Exemples d’utilisation :
$> python exo.py Ceci est le monde qui contient Charlie un homme sympa Charlie
6


$> python exo.py test test test
0

$> python exo.py test boom
-1

Afficher error et quitter le programme en cas de problèmes d’arguments.


"""
#Fonction
def afficheIndex(t):

    i = 0
    while i < len(t)-1:
        i = i + 1

    y = 0
    while t[i] != t[y]:
        y += 1
            
    print(y)

#Parsing
x = input("\n")
tableau = x.split(" ")

#Gestion d'erreur


#Affichage
afficheIndex(tableau)
