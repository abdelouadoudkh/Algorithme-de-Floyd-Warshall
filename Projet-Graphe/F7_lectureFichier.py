# Lecture du graphe
import math

def read_graphe(fichier):
    lines = []
    try:
        with open(fichier,'r') as f:
        # Stocker toutes les lignes du fichier dans un array
            for line in f:
                lines.append(line.replace("\n",""))
    except:
        print("Erreur dans la lecture du fichier")
        return []

    if len(lines)==0:
        print("Erreur dans la lecture du fichier, le fichier est vide")
        return []
    # Obtenir le nombre de sommets et d'arcs
    N_sommets = int(lines[0])
    N_arcs = int(lines[1])

    # Initialiser les matrices avec des inf,0 ou False
    matrice_adjacence_poids=[]
    for i in range(N_sommets):
        line_poids=[]
        line_bool=[]
        for j in range(N_sommets):
            if i == j:
                line_poids.append(0)
            else:
                line_poids.append(math.inf)
            line_bool.append("False")
        matrice_adjacence_poids.append(line_poids)

    # Stocker les arcs dans les deux matrices
    for i in range(2, 2 + N_arcs):
        tokens = lines[i].split()
        sommet_depart=int(tokens[0])
        sommet_arrive=int(tokens[1])
        poids=int(tokens[2])

        matrice_adjacence_poids[sommet_depart][sommet_arrive] = min(poids, matrice_adjacence_poids[sommet_depart][sommet_arrive])
    # Retourner les 2 matrices sous la forme d'une tuple
    return matrice_adjacence_poids
