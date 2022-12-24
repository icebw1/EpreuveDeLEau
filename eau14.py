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
    triParOrdreASCII(tableau)

#Gestion d'erreur
except ValueError:
    print("Erreur, la valeur entree est une chaine")
    exit()
