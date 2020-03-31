from NodoGenerico import NodoGenerico
from queue import PriorityQueue


class NodoParticular(NodoGenerico):
    def __init__(self, valor, padre, inicio=0, objetivo=0):
        super().__init__(valor, padre, inicio, objetivo)
        self.costo = 0
        self.dist = self.getDist()
        self.paso = 1

    def getDist(self):
        if not self.padre:
            self.costo = 0
        else:
            # Prueba de distintas funciones de costo
            self.costo = self.padre.costo+1
            ##for i in range(6):
            #    self.costo += abs(self.padre.valor[i] - self.valor[i])
        heur = 0
        for i in range(6):
            heur += abs(self.objetivo[i] - self.valor[i])
        dist = heur + self.costo
        return dist

    def crearHijos(self):
        for i1 in ([-1, 0, 1]):
            for i2 in ([-1, 0, 1]):
                for i3 in ([-1, 0, 1]):
                    for i4 in ([-1, 0, 1]):
                        for i5 in ([-1, 0, 1]):
                            for i6 in ([-1, 0, 1]):
                                q1 = self.valor[0] + i6 * self.paso
                                q2 = self.valor[1] + i5 * self.paso
                                q3 = self.valor[2] + i4 * self.paso
                                q4 = self.valor[3] + i3 * self.paso
                                q5 = self.valor[4] + i2 * self.paso
                                q6 = self.valor[5] + i1 * self.paso
                                valor = [q1, q2, q3, q4, q5, q6][:]
                                hijo = NodoParticular(valor, self)
                                self.hijos.append(hijo)


class AEstrella:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.objetivo = objetivo
        self.cola = PriorityQueue()
        self.nodosVisitados = []
        self.camino = []

    def solve(self):
        nodo_raiz = NodoParticular(self.inicio, 0, self.inicio, self.objetivo)
        contador = 0
        self.cola.put((nodo_raiz.dist, contador, nodo_raiz))
        while self.cola.qsize() and not self.camino:
            nodo_actual = self.cola.get()[2]
            if nodo_actual.valor == nodo_actual.objetivo:
                self.camino = nodo_actual.camino
                break
            nodo_actual.crearHijos()
            self.nodosVisitados.append(nodo_actual.valor)
            for hijo in nodo_actual.hijos:
                if hijo.valor not in self.nodosVisitados:
                    contador += 1
                    self.cola.put((hijo.dist, contador, hijo))
        if not self.camino:
            print("No se encontró ningún camino")
        return self.camino


pos_init = [0, 0, 0, 0, 0, 0][:]
pos_final = [3, 2, 1, 1, 3, 2][:]
a = AEstrella(pos_init, pos_final)
camino1 = a.solve()
for i in range(len(camino1)):
    string = str(i) + ") " + str(camino1[i])
    print(string)
