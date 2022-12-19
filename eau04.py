"""
Exercice : Prochain nombre premier
(slide 7)

Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.


Exemples d’utilisation :
$> python exo.py 14
17
$>

Afficher -1 si le paramètre est négatif ou mauvais.

"""
#Fonction 
def Premier(a):
    a = a + 1
    i = 2
    while i < a:
        resultat = a % i
        if resultat == 0:
            a = a + 1
        
        else:
            print(str(a))
            exit()
        i = i + 1
    
#Parsing 
try:
    print("Taper la valeur du nombre")
    x = int(input())


    if x == 0 or x == 1:
        x = 2

    #Resolution
    print(Premier(x))

#Gestion d'erreur
except ValueError:
    print("-1")
    exit()
