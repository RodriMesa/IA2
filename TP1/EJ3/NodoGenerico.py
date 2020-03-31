class NodoGenerico(object):
    def __init__(self,valor,padre,inicio=0,objetivo=0):
        self.valor = valor
        self.hijos = []
        self.padre = padre
        if not self.padre:
            self.inicio = inicio
            self.objetivo = objetivo
            self.camino = [valor]
        else:
            self.inicio = padre.inicio
            self.objetivo = padre.objetivo
            self.camino = padre.camino[:]
            self.camino.append(valor)

    def getDist(self):
        pass

    def crearHijos(self):
        pass