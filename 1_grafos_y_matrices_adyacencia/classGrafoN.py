class GrafoN:
    # Se guardan los grafos
    def __init__(self):
        self.verticesGrafos = [] # Los indices representan vertices de un grafo
        self.aristasGrafos = [] # Los indices representan vertices de un grafo
        self.cantidad = 0

    def reset(self):
        self.verticesGrafos = []
        self.aristasGrafos = []
        self.cantidad = 0

    def AddGrafo(self, verticesx, aristasx):
        self.verticesGrafos.append(verticesx)
        self.aristasGrafos.append(aristasx)
        self.cantidad += 1

    def ValidarPosicion(self, x):
        if(x>0 and x<=self.cantidad):
          return True
        else:
          return False
