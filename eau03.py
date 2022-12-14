"""
Exercice : Suite de Fibonacci
(slide 6)

Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et 
le premier élément étant à l’index 0.


Exemples d’utilisation :
$> python exo.py 3
2
$>

Afficher -1 si le paramètre est négatif ou mauvais.

"""
#Fonction : Suite de Fibonacci
x = 0
y = 1

tableau = []

def Fibonacci(a, b, c):

    #print("L'élément de la suite de Fibonacci n°1 est " + str(a))
    tableau.append(a)

    #print("L'élément de la suite de Fibonacci n°2 est " + str(b))
    tableau.append(b)

    resultat = a + b                                          
    #print("L'élément de la suite de Fibonacci n°3 est " + str(resultat))
    tableau.append(resultat)

    newResultat = resultat + b                                 
    #print("L'élément de la suite de Fibonacci n°4 est " + str(newResultat))
    tableau.append(newResultat) 

    i = 5
    while i < 100:

        resultat = newResultat + resultat  
        #print("L'élément de la suite de Fibonacci n°" + str(i) + " est " + str(resultat))
        tableau.append(resultat) 

        newResultat = resultat + newResultat   
        #print("L'élément de la suite de Fibonacci n°" + str(i+1) + " est " + str(newResultat))
        tableau.append(newResultat) 

        i = i + 2

    print("L'élément " + str(z) + " de la suite de Fibonacci est " + str(tableau[c]))


#Parsing 
z = int(input("Ce programme affiche le N-ème élément de la suite de Fibonacci, taper un nombre "))

#Gestion d'erreur
if type(z) == str:
    print("Erreur, vous n'avez pas tapé un nombre")
    exit()

#Resolution
Fibonacci(x, y, z)
