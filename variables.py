# une variable est une boite qui contient une valeur 
# celle ci peut changer au cours du programme

# quelque chose = à quelque chose

maVariable1 = 15 # nombre entier (/int)
maVariable2 = "bonjour" # lettres (/str) (string=ficelle=chaîne de caractères)
maVariable3 = 0.5 # nombre decimal (/float)

maListe = ["Bonsoir","Salut", 42] # une liste contenant 3 valeurs => 0,1,2

# un dictionnaire contenant 3 valeurs
# sa particularité c'est que les indexes sont choisi par nous meme
monDico = {"a" : "rate", 
           "b" : 42, 
           "c" : 0.15}

# Ici, on affiche dans le terminal les valeurs et les types
# de chaque variable (attention aux listes et dictionnaires)
print(maVariable1, type(maVariable1))
print(maVariable2, type(maVariable2))
print(maVariable3, type(maVariable3))
print(maListe[0], type(maListe))
print(monDico["a"], type(monDico))
print("----------------------------------------------")
# operateurs arithmetique 
# + : addition 
# - : soustraction 
# / : division 
# * : multiplication 
# ** : exposant 
# // : division entiere (exemple: 4.5 devient 4, on vire la virgule)
# % : modulo (exemple: 9 diviser en 2 = 4.5, 4.5 devient 4, on garde le reste = 0.5 arrondie à 1)
print(maVariable1**2)
print(maVariable1//2)
print(maVariable1%2)
autreVariable = maVariable1%2 # on stock le resultat dans une autre 

print("----------------------------------------------")
# operateurs de comparaison
# > : symbol "plus grand"
# < : symbol "plus petit"
# >= : plus petit ou egale a
# <= : plus petit ou egale a
# == : est egal a
# != : est different que 

if (5<10):
    print("vrai")
if(maVariable1 == 15):
    print("vrai")
if (15 != maVariable1): #celui ci sera ignore car ils sont egale
    print("vrai")
