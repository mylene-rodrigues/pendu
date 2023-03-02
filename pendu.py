import random #bibliotèque au hasard

#choisi un mot
mots = []
with open("mots.txt") as fl:  #ouvre le fichier et donne l'accès à tte les lignes
    for l in fl: #chaque ligne une par une
        mots.append(l.rstrip("\n")) # \n revient à la ligne

#choisir un mot au hasard
mot = random.choice(mots) #prend un élément au hasard de la liste

#variable cle

lettres = [] #liste qui garde toutes les lettres que l'utilisateur à donné
faux = 0 # combien de lettre deviné ne sont pas ds le mot
trouve = False #savoir si l'utilisateur à gagné

while not trouve:
    trouve = True
    print("+---+")
    print(" |  |")
    print(" |   o")
    print(" |  /|/")
    
    for l in mot: #va à travers ttes les lettres du mots
        if l in lettres: # si la lettre est à l'intérieur des lettres que l'utilisateurs à deviné
            print(l, end="")#imprimer la lettre
        else : #si la lettre est pas dsles lettres devinés, la barre
            trouve = False
            print("_", end="") #end ==> remplace ce caractère de nouvelle ligne par un espace
    
    if faux > 7:
        print("Tu as perdu!")
        break
    
    if trouve:
        print("Tu as gagné!")
        break #pas nécessaire

    lettres = input("Entrez une lettre: ")
    lettres.append(lettre)

    if lettres not in mot:
        faux += 1 #si la lettre n'est pas ds le mot, on rajoute 1 à faux
    #une lettre
    #mot?
    #gagné/perdu/continuer




