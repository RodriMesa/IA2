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
    layout = armar_espacio(2,2)
    #valor_init=tuple(random.sample(range(1,layout["Val_max"]+1),random.randint(1,layout["Val_max"])))
    valor_init=(1,3,4,2,5,22)
    a = Temple(15, 1500, valor_init, layout)
    solucion = a.solver()
    print(solucion[2])
    plt.plot(range(1,len(solucion[3])+1),solucion[3])
    plt.xlabel('Iteraciones')
    plt.ylabel('Costo')
    plt.title('Algoritmo de Temple')
    plt.grid()
    plt.show()

if __name__=='__main__':
    main()