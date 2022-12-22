"""
Exercice : Chiffres only
(slide 11)

Créez un programme qui détermine si une chaîne de caractères ne contient que des chiffres.

Exemples d’utilisation :
$> python exo.py “4445353”
true


$> python exo.py 42
true

$> python exo.py “Bonjour 36”
false

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""
#Fonction
def queDesChiffres(t):
    print("true") 

#Parsing
x = input("\n")

#Gestion d'erreur
if not x.isdigit():
    print("false") 
    exit()

#Affichage
queDesChiffres(x)
