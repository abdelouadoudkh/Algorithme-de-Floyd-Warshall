from F7_copyMatrice import copy

def show(matrice_input, header=""):
    matrice=copy(matrice_input)
    # Calculer la longeur maximale de toute la matrice
    # Initialisation au nombre de char du summet le plus grand
    max_len=len(str(len(matrice)))
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            size=len(str(matrice[i][j]))
            if size>max_len:
                max_len=size
    # Interer la matrice et remplacer chaque valeur(soit int ou str) par une str de la 
    # longeur qu'on vient de calculer
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            # Obtenir le valeur en forme de string et sa longeur
            string=str(matrice[i][j]).strip()
            size=len(string)

            # Si la taille est maximale on passe
            if(size==max_len):
                pass

            # Sinon on ajoute autant de " " que neccessaires
            else:
                for k in range(max_len-size):
                    string+=" "
            
            # On garde la  nouvelle valeur dans la matrice
            matrice[i][j]=string


    # Ayant calculé la taille max, on ajoute une ligne pour montrer les sommets, si bien qu'0'une cologne pour le même
    line0 = []
    # On ajoute le space du coin superieure gauche
    space=""
    for x in range(max_len):
        space+=" "
    line0.append(space)

    # Création du numero du sommet en respectant la longeur max
    for k in range(len(matrice)):
        size_k=len(str(k))
        string = str(k)
        if(size_k==max_len):
            pass
        else:
            for x in range(max_len-size_k):
                string+=" "

        # On ajoute le numero du sommet à la premiere ligne
        line0.append(string)

        # On ajoute le numero du sommet au debut de chaque ligne
        matrice[k].insert(0,string)
    # Ajouter la premiere ligne à la matrice
    matrice.insert(0,line0)


    
    # Impression de la matrice
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            matrice[i][j]=str(matrice[i][j])
    print("\n===================================================================")
    if(header!=""):
        print(str(header))
    for line in matrice:
        print("\t".join(line))
    print("===================================================================\n")
