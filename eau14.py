"""
Exercice : Par ordre Ascii
(slide 17)

Créez un programme qui trie les éléments donnés en argument par ordre ASCII.

Exemples d’utilisation :
$> python exo.py Alfred Momo Gilbert
Alfred Gilbert Momo

$> python exo.py A Z E R T Y
A E R T Y Z

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""
#Fonction
def triParOrdreASCII(t):
    i = 0
    j = 0   
    while i <= len(t)-j:     #Après le 1er parcous, le plus grand nb étant à sa position définitive (en dernier) : il n'a plus à être traité. 
            if i == len(t)-1:
                i = 0
                j = j + 1

            if t[i] <= t[i+1]:
                (t[i], t[i+1]) = (t[i], t[i+1])

            elif t[i] > t[i+1]:
                (t[i], t[i+1]) = (t[i+1], t[i])

            i = i + 1
    for n in t:
        print(end=n + " ")

try:
    #Parsing
    x = input("Ce programme trie une liste de mots (Tri par ordre Ascii).\n")
    tableau = x.split(" ")

    #Affichage
    triParOrdreASCII(tableau)

#Gestion d'erreur
except ValueError:
    print("Erreur")
    exit()
