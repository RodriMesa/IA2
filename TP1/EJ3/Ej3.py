from Astar import Asolver
from Layout import armar_espacio
import matplotlib.pyplot as plt
import numpy
import time


def main():
    start_time= time.time()
    matriz = armar_espacio(100, 150)
    mat=numpy.zeros((matriz["Filas"],matriz["Columnas"]))
    valor_inicio = 1
    valor_objetivo = matriz["Val_max"]
    if (matriz["Val_max"] >= valor_inicio > 0):
        if matriz["Val_max"] >= valor_objetivo > 0:
            a = Asolver(valor_inicio, valor_objetivo, matriz)
            camino= a.solver()
            for i in camino[0]:
                print(i)
            print("Costo: ", round(camino[1]/0.7))
            for indice in matriz:
                if matriz[indice]!="Pasillo" and indice!="Filas" and indice!="Columnas" and indice!="Val_max":
                    mat[indice[0]][indice[1]]=5
            mat[camino[0][0][0]][camino[0][0][1]]=10
            mat[camino[0][len(camino[0])-1][0]][camino[0][len(camino[0])-1][1]]=10
            for camino in camino[0][1:len(camino[0])-1]:
                mat[camino[0]][camino[1]]=8
            plt.imshow(mat)
            print("--- %s seconds ---" % (time.time() - start_time))
            plt.show()
        else:
            print("Estas por fuera del espacio de trabajo")
    else:
        print("Estas por fuera del espacio de trabajo")
if __name__=='__main__':
    main()