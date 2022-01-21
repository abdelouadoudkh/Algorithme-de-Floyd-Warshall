from F7_copyMatrice import copy
from F7_impressionMatrice import show
import math

# Algorithme Floyd-Warshall
def AlgoFloydWarshall(matrice_input):
    # Matrice avec les poids
    matriceL=copy(matrice_input)

    # Matrice avec les chemins
    matriceP=[]

    # Initialisation de la matriceChemins
    for i in range(len(matriceL)):
        line_aux=[]
        for j in range(len(matriceL)):
    
            if(matriceL[i][j]==math.inf):
                line_aux.append("Null")
            else:
                line_aux.append(i)   
        matriceP.append(line_aux)
    for k in range(len(matriceL)):
        for i in range(len(matriceL)):
            for j in range(len(matriceL)):
                if (matriceL[i][k] + matriceL[k][j] < matriceL[i][j]):
                    matriceL[i][j] =  matriceL[i][k] + matriceL[k][j]
                    matriceP[i][j] = matriceP[k][j]
        print("Iteration :", k)
        show(matriceP,"matriceP")
        show(matriceL,"matriceL")
    return matriceL,matriceP




def afficherChemins(matriceP, matriceL):
# Copier la matrice, obtenir le numero de sommets
    matrice = copy(matriceP)
    num_sommets=len(matrice)
    circuit_absorbant=False

# Voir si le graphe a des circuits absorbants
    for i in range(num_sommets):
        if(matriceL[i][i] < 0):
            print("===================================================================")
            print("Le graph contient des circuits absorbants. L'affichage des chemins n'est pas possible")
            print("===================================================================")
            circuit_absorbant=True
            break
    # Si le graphe a des circuits absorbants, on n'execute rien
    if(circuit_absorbant==False):
        print("===================================================================")
        print("Le graph ne contient pas des circuits abosrbants, l'affichage des chemins est possible")
        print("===================================================================")
        arreter_boucle=False
        
        # Boucle pour demander le chemin
        while not arreter_boucle:
            print("\nTapez le sommet de depart, tapez 'sortir' pour finir l'affichage des chemins et passer a un autre graphe")
            sommet_depart=input("Sommet de depart: ")
            
            # Retourner à la selection de graphe si on tape 'sortir'
            if(sommet_depart=="sortir"):
                break
            sommet_arrive=input("Sommet d'arrivée: ")
            
            try:
                # Essayer de les convertir en int
                sommet_depart=int(sommet_depart)
                sommet_arrive=int(sommet_arrive)

                # S'assurer que les sommets depart et arrivé existent dans le graphe
                if(sommet_depart>num_sommets-1 or sommet_arrive> num_sommets-1):
                    print("Sommets out of range")
                
                # Si c'est le cas, afficher le chemin
                else:
                    if(sommet_depart==sommet_arrive):
                        print("Sommet de depart et sommet d'arrivé ne peuvent pas être le même")                       
                     #  S'assurer qu'il existe un chemin
                    elif(matrice[sommet_depart][sommet_arrive]=="Null"):
                        print("Il n'existe pas un chemin entre ces deux sommets")
                    else:
                        ''' This is a multiline comment. lgorithme: regarder dans la matrice la position [sommet_depart][sommet_arrivé]. Ça nous donne le sommet precedent au sommet arrivé.
                        On cherche iterativement la position [sommet_depart][sommet_actuel] pour trouver tous les predeceseurs jusqu'à qu'on arrive au sommet depart '''
                        
                        # S'il existe, executer l'algorithme pour le trouver, le garder dans chemin[]  
                        chemin = []
                        # On initialise le chemin avec le sommet_arrive   
                        chemin.append(str(sommet_arrive))
                        sommet_actuel = sommet_arrive
                        
                        
                        while(sommet_actuel!=sommet_depart):
                            sommet_actuel=int(matrice[int(sommet_depart)][int(sommet_actuel)])
                            chemin.append(str(sommet_actuel))
                        
                        # On inverse le chemin pour commencer par le sommet_depart
                        chemin.reverse()
                        print("Chemin entre", sommet_depart, "et", sommet_arrive,": " + " --> ".join(chemin) , "de chemin total : " ,
                                matriceL[sommet_depart][sommet_arrive])
            except:
                print("Sommets non reconnus, veuillez recommencer")
