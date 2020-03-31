#Imports standart
import random
import time
import matplotlib.pyplot as plt
import numpy as np
import time
#Imports locales
from Astar import Asolver
from Layout import armar_espacio
from temple import Temple
from NodoTemple import NodoTemple


def main():
    start_time = time.time()
    valor_init = (3,1,4,2,48,21,33,73,21)
    layout = armar_espacio(4,4)
    a = Temple(40, 0.01, valor_init, layout)
    valores=[]
    for _ in range(100):
        solucion = a.solver()
        valores.append(solucion[1])
    plt.hist(valores, bins= 'auto', color= '#0504aa',
    alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma')
    plt.text(23, 45, r'$\mu=15, b=3$')
    print("--- %s seconds ---" % (time.time() - start_time))
    plt.show()

if __name__=='__main__':
    main()