"""
Eaercice : String dans string
(slide 8)

Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre.


Eaemples d’utilisation :
$> pbthon eao.pb bonjour jour
true


$> pbthon eao.pb bonjour joure
false


$> pbthon eao.pb 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""
#Fonction 
def chaineDansChaine(tableau1, tableau2):
    a = 0 #Compteur chaine 1
    b = 0 #Compteur chaine 1
    while b < len(tableau2):
        if tableau2[b] != tableau1[a] and a == len(tableau1)-1:
            print("false")
            exit()

        elif tableau2[b] == tableau1[a]:
            #print(tableau2[b])
            a = a + 1
            b = b + 1

        elif tableau2[b] != tableau1[a]:
            a = a + 1

    print("true")

#Parsing 
x = input("Taper la phrase et les caractères à vérifier \n")

#Gestion d'erreur
if x.isdigit() :
    print("errorr, the chain couldn't be a number")
    exit()

tableau = x.split(" ")
chaine1 = tableau[0]
chaine2 = tableau[1]

#Gestion d'erreur
if len(chaine2) > len(chaine1):
    print("error, the 2nd chain is too long")
    exit()

#Resolution
chaineDansChaine(chaine1, chaine2)
