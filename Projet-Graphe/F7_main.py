from F7_impressionMatrice import *
from F7_lectureFichier import *
from F7_copyMatrice import copy
from F7_algorithme import *
from os import listdir

# Fonction pour selectioner un graphe
def selectGraph():
    # Lire les fichiers de 'graphes/'. Si c'est vide l'execution termine
    graphes=[]
    try:
        graphes = listdir("F7_graphes")
    except:
        print("Erreur dans la lecture du ficher des graphes")
        exit()
    
    # Supprimer de la liste des graphes des dossiers ou fichiers non ".txt"
    for fich in graphes:
        if (not(".txt" in fich)):
            graphes.remove(fich)

    if graphes==[]:
        print("il n'y a pas des fichiers '.txt' à lire")
        print("Exit...")
        exit()
    
    num_graphs=len(graphes)
    chosen=None
    break_condition=False

    # On a une boucle jusqu'au moment ou il y a un choix du graph correct  
    while not break_condition:
        print("Choisisez un graph pour le lire, tapez 'end' pour finir l'execution:")
        # Impression des possibilités   
        for i in range(num_graphs):
            g=graphes[i]
            print(i,"\t---> ",g)
        print("end\t--->  exit()")
        # Lire le choix
        chosen=input("choix: ")

        # Finir l'execution si on tape 'end'
        if chosen=="end":
            print("Exit...")
            exit()
        
        # Sinon on essaye de lire le numero reçu
        try:
            chosen=int(chosen)
        except:
            pass
        
        # Si le numero appartient aux options possibles on sort de la boucle
        if chosen in range(num_graphs):
            break_condition=True
        
        # Sinon on continue à demander une option correcte
        else:
            print("Choix non reconnu, essayez de nouveau")
    return graphes[chosen]

        
# Entrée du programme
if __name__ == '__main__':
    print("\n====================================================================\n")
    print("F7 Projet SM501 - Automates finis, graphes, expressions rationnelles")
    print("\nProgramme developpé par:\n\t-AOUFI Yassir\n\t-AUMAITRE Christopher\n\t-KHOUNA Abdelouadoud\n\t-MEZIANE Oussama\n\t-PLANAS THIRIET Ignacio")
    print("\n====================================================================\n")
    
    # boucle d'execution principal du programme
    while True:
        # Choix du graphe à lire
        currentGraph = selectGraph()
        print("Lecture du fichier 'F7_graphes/" + currentGraph + "'")
        matrice_adjacence_poids = read_graphe("F7_graphes/"+currentGraph)        
        
        # Si les matrices sont vides, c'est-à-dire s'il y a eu un erreur, selectioner un autre graphe
        if(matrice_adjacence_poids==[]):
            print("Graphe non valide")
            continue

        show(matrice_adjacence_poids,"Matrice d'adjacence du graphe")
        matriceL ,matriceP = AlgoFloydWarshall(matrice_adjacence_poids)
    
        afficherChemins(matriceP, matriceL)
