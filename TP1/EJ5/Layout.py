def armar_espacio(num_filas, num_columnas):
    filas_mat = 5*num_filas+1
    columnas_mat = 3*num_columnas+1
    mat = {}
    cont1 = 2
    cont2 = 1
    for j in range(columnas_mat):
        for i in range(filas_mat):
            if j%3 and j!=0 and i%5 and i!=0:
                    if (j-1)%3 and not j-1==0:
                        mat[(i, j)] = cont1
                        cont1 += 2
                    if (j+1)%3:
                        mat[(i, j)] = cont2
                        cont2+=2
            else:
                mat[(i, j)] = "Pasillo"
    mat["Filas"] = filas_mat
    mat["Columnas"] = columnas_mat
    mat["Val_max"] = (num_columnas*num_filas*8)
    return mat