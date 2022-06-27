import sys
import options as init
import classGrafoN as gn
import classGrafoWithMetod as g

if __name__ == '__main__':
    Grafo = g.Grafo()
    Grafos = gn.GrafoN()
    init.option(Grafo, Grafos)
    sys.exit()

#Se debe ejecutar este archivo python para empezar