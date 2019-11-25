# operateurs de comparaison
# > : symbol "plus grand"
# < : symbol "plus petit"
# >= : plus petit ou egale a
# <= : plus petit ou egale a
# == : est egal a
# != : est different que 

#les conditions
# if () : SI la condition est vrai
# elif () : SINON SI cette condition est vrai
# else : SINON, par defaut tu fais...
# on peut utiliser soit l'un des 3 
# soit 2 des 3 soit les 3 en meme temps (voir plus) 
age = 16 

if (age < 12):
    print("enfant")
elif(age < 18):
    print("ado")
else :
    print("adulte")

    print("---------------------------------------")
    # les boucles 
    # while () : TANT QUE (la condition est vrai)
    # for () : POUR CHAQUE element DANS ma liste...

compteur = 1

while (compteur <= 10):
    print(compteur)
    compteur = compteur + 1

maListe = ["C'est","enfin","fini"]
for element in maListe:
    print(element)
