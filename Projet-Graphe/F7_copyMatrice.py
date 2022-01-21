def copy(matrice):
    matrice_aux=[]
    for line in matrice:
        line_aux=[]
        for value in line:
            line_aux.append(value)
        matrice_aux.append(line_aux)
    return matrice_aux