import numpy as np
import networkx as nx 

class Grafo:
    # Se resetea los vertices y matriz para ser ingresado nuevamente
    def __init__(self):
        self.vertices = []
        self.aristas = []
        self.matriz = [[None] * 0 for i in range(0)]

    # Se resetea los vertices y matriz para ser ingresado nuevamente
    def reset(self):
        self.vertices = []
        self.aristas = []
        self.matriz = [[None] * 0 for i in range(0)]

    # Verifica si el usuario que ingresó el vertice existe o no en opcion 1 (aristas) y 5 del menu
    def comprobacion_vertice(self, vertice):
      for i in self.vertices:
        if(i == vertice):
          return True
      return False

    # Verifica si el usuario ingresó el peso de una arista correctamente
    def comprobacion_tipo(self, x):
      try:
            x = int(x)
            return True
      except ValueError:
            return False
    
    # Verifica si el vertice ingresado ya está en la matriz
    def isVertice(self, v):
        if (self.matriz.count(v) == 0):
            return False
        return True     
      
    # Añade un vertice a la matriz
    def addVertice(self, v):
        if (self.isVertice(v)):
            return False
        self.vertices.append(v)
        
        # Preparando la matriz de adyacecia
        
        filas = columnas = len(self.matriz)
        matriz_aux = [[None] * (filas + 1) for i in range(columnas + 1)]

        for f in range(filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[f][c]

        self.matriz = matriz_aux
        return True

    #Añade una arista con su respectivo peso en la matriz
    def addArista(self, inicio, fin, peso):
        if not (self.isVertice(inicio) or not (self.isVertice(fin))):
            return False

        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = peso
        # Para grafos no dirigidos
        self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = peso
        return True

    # Añade un listado de aristas
    def addAristaList(self, a):
      self.aristas.append(a)
      
    
    def ciclico(self):
       largo = len(self.aristas)
       arista_inicial = self.aristas[0]
       arista_final = self.aristas[largo-1]
       if(arista_inicial[0] == arista_final[1]):
         return True
       return False
    
    def camino_euleriano(self):
      G = nx.DiGraph()
      G.add_nodes_from(self.vertices)
      for ar in self.aristas:
        G.add_edge(ar[0], ar[1], capacity=int(ar[2]))
      is_eu = nx.is_eulerian(G)    
      if(is_eu):
        return True
      return False    
      
    # Imprime la matriz del Grafo
    def imprimir_matriz(self, m):
        cadena = "\n"
        for c in range(len(m)):
            cadena += "\t" + str(self.vertices[c])
        cadena += "\n" + ("        -" * len(m))
        for f in range(len(m)):
            cadena += "\n" + str(self.vertices[f]) + " |"
            for c in range(len(m)):
                if ((f == c) and (m[f][c] is None or m[f][c] == 0)):
                    cadena += "\t" + "0"
                else:
                    if (m[f][c] is None):
                        cadena += "\t" + "0"
                    else:
                        cadena += "\t" + "1"
        cadena += "\n"
        print(cadena)
    
    #Revisa si es conexo o no el grafo
    def isConexo(self):
        filas = columnas = len(self.matriz)
        # Matriz de peso para el calculo
        matriz_aux = [[0] * (filas) for i in range(columnas)]
        for f in range(filas):
            for c in range(columnas):
                if (self.matriz[f][c] is None):
                    matriz_aux[f][c] = 0
                else:
                    matriz_aux[f][c] = int(self.matriz[f][c])
        # Matriz identidad
        matriz_identidad = [[0] * (filas) for i in range(columnas)]
        for f in range(filas):
            for c in range(columnas):
                if (f == c):
                    matriz_identidad[f][c] = 1
                else:
                    matriz_identidad[f][c] = 0
        ma = np.matrix(matriz_aux)
        C = np.matrix(matriz_identidad)
        for i in range(filas - 1):
            C_aux = ma
            while(i > 0):
                C_aux = C_aux * ma
                i = i - 1
            C = C + C_aux      
        # Pregunto si hay algun 0
        if(np.any(C == 0)):
            return False
        else:
            return True       
          
    #Caminos de largo n para el grafo
    def Caminos(self, caminos):
        filas = columnas = len(self.matriz)
        #Matriz de adyacencia con numeros enteros 1 y 0
        matriz = [[0] * (filas) for i in range(columnas)]
        for f in range(filas):
            for c in range(columnas):
                if (self.matriz[f][c] is None):
                    matriz[f][c] = 0
                else:
                    matriz[f][c] = 1
        # Matriz de identidad
        matriz_identidad = [[0] * (filas) for i in range(columnas)]
        for f in range(filas):
            for c in range(columnas):
                if (f == c):
                    matriz_identidad[f][c] = 1
                else:
                    matriz_identidad[f][c] = 0
        if(int(caminos) > int(filas)):
            #No puede existir caminos de ese largo para la matriz dada
            print("No existen caminos de ese largo para el grafo dado")
        elif(caminos == 0):
            for f in range(filas):
                for c in range(columnas):
                    if(matriz_identidad[f][c] != 0):
                        print(self.vertices[f] + "->" + self.vertices[c] + "  Cantidad de caminos: " + str(matriz_identidad[f][c]))
        elif(caminos == 1):
            for f in range(filas):
                for c in range(columnas):
                    if(int(matriz[f][c]) != 0):
                        print(self.vertices[f] + "->" + self.vertices[c] + "  Cantidad de caminos: " + str(matriz[f][c]))
        else:
            matriz = matriz_aux = np.matrix(matriz)
            i = 0
            while(i < int(caminos)-1):
                matriz = matriz * matriz_aux
                i = i + 1
            matriz = matriz.tolist()
            #print(matriz)  mostramos matriz para ejemplo
            for f in range(filas):
                for c in range(columnas):
                    if(int(matriz[f][c]) != 0):
                        print(self.vertices[f] + "->" + self.vertices[c] + "  Cantidad de caminos: " + str(matriz[f][c]))
  
  
    def dijkstra(self, v_inicial):
        if(self.vertices.count(v_inicial) == 0):
            print("El nodo que ha ingresado no pertenece al grafo")
        else:
            filas = columnas = len(self.matriz)
            #Matriz de peso con enteros
            matriz = [[0] * (filas) for i in range(columnas)]
            for f in range(filas):
                for c in range(columnas):
                    if(self.matriz[f][c] is None):
                        matriz[f][c] = 0
                    else:
                        matriz[f][c] = int(self.matriz[f][c])

            #Crea un array de numpy para analizar la matriz mas facilmente
            matriz = np.array(matriz)
            #Crea el grafico de la libreria networkx para usar sus metodos (Dijkstra)
            G = nx.from_numpy_matrix(matriz, create_using=nx.DiGraph())
            pred, dist = nx.dijkstra_predecessor_and_distance(G, self.vertices.index(v_inicial))
            dist = dist.items()
            #print(pred) #Antecesores como diccionario
            #print(pred.items()) #Antecesores como arreglo
            for i in dist:
                #Rearmando la ruta
                #Codigo del rearme de ruta (In progress...)
                #Distancias (working...)
                print("Distancia menor de " + v_inicial + "->" + self.vertices[i[0]] + ": " + str(i[1]))