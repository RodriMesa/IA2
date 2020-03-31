from NodoAstar import NodoAstar
from queue import PriorityQueue


class Asolver:
    def __init__(self, inicio, objetivo, matriz):
        list1 = list(matriz.keys())
        list2 = list(matriz.values())
        self.inicio = list1[list2.index(inicio)]
        self.objetivo = list1[list2.index(objetivo)]
        del list1
        del list2
        self.matriz = matriz
        self.nodosVisitados = []
        self.camino = []
        self.cola = PriorityQueue()

    def solver(self):
        nodo_init = NodoAstar(self.inicio, 0, self.matriz, self.inicio, self.objetivo)
        cont = 0
        costo = 10000
        self.cola.put((nodo_init.dist, cont, nodo_init))
        while self.cola.qsize() and not self.camino:
            nodo = self.cola.get()[2]
            if nodo.valor == nodo.objetivo:
                self.camino = nodo.camino
                costo = nodo.costo
                break
            nodo.crearHijos()
            self.nodosVisitados.append(nodo.valor)
            for hijo in nodo.hijos:
                if hijo.valor not in self.nodosVisitados:
                    cont += 1
                    self.cola.put((hijo.dist, cont, hijo))
        if not self.camino:
            print("No se ha encontrado solución")
        return [self.camino, costo]