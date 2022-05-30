import os
import numpy as np
import networkx as nx 

print('MATRICES DE ADYACENCIA DE GRAFOS\n')

def menu():
    print(' ------------------------------- ')
    print('1. Ingresar Grafo')
    print('2. Mostrar Matriz de Adyacencia')
    print('3. Imprimir cantidad de vertices y aristas')
    print('4. Tipo de grafo (conexo, ciclico, euleriano)')
    print('5. Caminos')
    print('6. Dijkstra')
    print('7. Isomorfismo, se requiere 2 grafos ingresado, de lo contrario se omitira')
    print('8. Resetear todos los grafos')
    print('9. Eligir un grafo registrado para opciones 2, 3, 4, 5 y 6')
    print('10. Flujo Maximo')
    print('11. Numero cromatico y coloreo')
    print('12. Árbol Kruskal, aplicable solo grafo conexo')
    print('13. Árbol Prim, aplicable solo grafo conexo')
    print('14. Salir')
    print(' ------------------------------- ')

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
      verticeP = Grafo.vertices
      aristasP = Grafo.aristas
      G = nx.DiGraph()
      G.add_nodes_from(verticeP)
      for ar in aristasP:
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
                    #           elif(math.isinf(m[f][c])):
                    #             cadena += "\t" + "∞"
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

#Aplicación para el algoritmo PRIM
def Prim(grafo, origen):
  # Se crea las estructuras de datos necesarias para
  # almacenar los datos necesarios.
  listaVisitados = []
  grafoResultante = {}
  listaOrdenada = []
  # Se agrega a una lista listaVisitados al nodo inicial
  listaVisitados.append(origen)

  # Se agrega las adyacencias del vertice inicial lista ordenada
  for destino, peso in grafo[origen]:
    listaOrdenada.append((origen, destino, peso))
  # Se aplica el método de ordenamiento de inserción
  pos=0
  act=0
  listAux=[]
  for i in range(len(listaOrdenada)):
      listAux=listaOrdenada[i]
      act=listaOrdenada[i][2]
      pos=i
      while pos> 0 and listaOrdenada[pos-1][2] > act:
          listaOrdenada[pos] = listaOrdenada[pos-1]
          pos=pos-1
      listaOrdenada[pos]=listAux
  # Se entra un bucle mientas la listaOrdenada no estuviera vacia
  while listaOrdenada:
    # Se toma un vertice de la lista ordenada y eliminarlo
    vertice = listaOrdenada.pop(0)
    d = vertice[1]
    # Se verifica que el destino no se ha visitado o tocado
    if d not in listaVisitados:
      # Se agrega a la lista de visitados en nodo destino
      listaVisitados.append(d)
      # Cabe mencionar que "d" corresponde a los nodos que no fueron visitados
      for key, lista in grafo[d]:
        if key not in listaVisitados:
          listaOrdenada.append((d, key, lista))
      # Se ordena el listado de aristas
      listaOrdenada = [(c,a,b) for a,b,c in listaOrdenada]
      listaOrdenada.sort()
      listaOrdenada = [(a,b,c) for c,a,b in listaOrdenada]
      # Se extrae el vertice inicial, destino y peso para agregar en
      # el grafo resultante de Prim
      origen  = vertice[0]
      destino = vertice[1]
      peso    = vertice[2]
      # Se verifica que el vertice inicial exista en grafo resultante
      if origen in grafoResultante:
        # Se verifica que el vertice destino exista en grafo resultante
        if destino in grafoResultante:
          lista = grafoResultante[origen]
          grafoResultante[origen] = lista + [(destino, peso)]
          lista = grafoResultante[destino]
          lista.append((origen, peso))
          grafoResultante[destino] = lista
        # En caso de que el vertice destino no exista en grafo resultante
        else:
          grafoResultante[destino] = [(origen, peso)]
          lista = grafoResultante[origen]
          lista.append((destino, peso))
          grafoResultante[origen] = lista
      # Se verifica que el vertice inicial no exista pero si resultante en grafo resultante
      elif destino in grafoResultante:
        grafoResultante[origen] = [(destino, peso)]
        lista = grafoResultante [destino]
        lista.append((origen, peso))
        grafoResultante[destino] = lista
      # En caso de que ambos nodos, vertices inicial y destino, no exista
      else:
        grafoResultante[destino] = [(origen, peso)]
        grafoResultante[origen] = [(destino, peso)]
      
  print("\n\nGrafo resultante:\n")
  for key, lista in grafoResultante.items():
    print(key)
    print(lista)


#Aplicación para el algoritmo KRUSKAL

# Función donde se crea conjunto en los vertices, asignando uno a un nodo
def Make_set(vertice, Nodo):
    Nodo[vertice] = vertice

# Funcion que permite buscar conjunto en los vertices
def Find_set(vertice, Nodo):
    if Nodo[vertice] != vertice:
        Nodo[vertice] = Find_set(Nodo[vertice], Nodo)
    return Nodo[vertice]
# Función que permite unir dos nodos formando una arista
def Union(u, v, Ordenada, Nodo):
    Dato1 = Find_set(u, Nodo)
    Dato2 = Find_set(v, Nodo)
    if Dato1 != Dato2:
        for Dato in Ordenada:
            Nodo[Dato1] = Dato2

def Algoritmo_Kruskal(grafo, Nodo):
# Se guarda las aristas resultantes
    resultante = []
    cont = 0
    # Se almacena los nodos desde el grafo ingresado
    for vertice in grafo['A']:
        Make_set(vertice, Nodo)
    # Se procede en ordenar la lista de aristas
    Ordenada = list(grafo['B'])
    Ordenada.sort()
    Ordenada = [(a,b,c) for c,a,b in Ordenada]
    print ("==============================")
    print ("Datos Ordenados")
    print("==============================")
    print("Ordenados:", Ordenada)
    Ordenada = [(c,a,b) for a,b,c in Ordenada]
    # Se recorre la lista de aristas que están ordenadas
    for Dato in Ordenada:
        peso, u, v = Dato
        # Se verifica que ambos nodos sean distintos
        if Find_set(u, Nodo) != Find_set(v, Nodo):
            # Se almacena al arista de menor peso
            resultante.append(Dato)
            print("==============================")
            print("Paso:", cont)
            print("==============================")
            resultante = [(a,b,c) for c,a,b in resultante]
            print("Resultante: ", resultante) 
            resultante = [(c,a,b) for a,b,c in resultante]
            cont+=1
            Union(u, v, Ordenada, Nodo)
    return resultante

def aplicacion_kruskal():
    Nodo = dict()
    resultado = {}
    #conjuntos = []
    aux = []
    for i in Grafo.aristas: #se recorre la arista
        aux.append((i[2], i[0], i[1]))
        grafo = {
        'A': Grafo.vertices,
        'B': aux
        } #se construye un diccionario
        # Se obtiene el resultado de árbol kruskal
        resultante = Algoritmo_Kruskal(grafo, Nodo)
        resultante = [(a,b,c) for c,a,b in resultante]
        for origen,destino,peso in resultante:
            # Se verifica que el vertice origen exista en el resultado 
            if origen in resultado:
                # Se verifica que el vertice destino exista en el resultado
                if destino in resultado:
                    lista = resultado[origen]
                    resultado[origen] = lista+[(destino,peso)]
                    lista = resultado[destino]
                    lista.append((origen,peso))
                    resultado[destino] = lista
                # En caso de que el vertice destino no exista en el resultado
                else:
                    resultado[destino] = [(origen,peso)]
                    lista = resultado[origen]
                    lista.append((destino,peso))
                    resultado[origen] = lista
            # En caso de que el vertice destino exista pero no el origen en el resultado
            elif destino in resultado:
                resultado[origen] = [(destino,peso)]
                lista = resultado[destino]
                lista.append((origen,peso))
                resultado[destino] = lista
            # En caso de que los vertices origen y destino no existan en el resultado
            else:
                resultado[destino] = [(origen,peso)]
                resultado[origen] = [(destino,peso)]
        print("\n=========Resultados=========")
        print("Arbol de expansion minima: ")
        for key, lista in resultado.items():
          print(key)
          print(set(lista))
        

Grafo = Grafo()
Grafos = GrafoN()

while True:
    menu()
    print("Actualmente, tienen ingresado", Grafos.cantidad, "grafos, para la opcion de isomorfismo se requiere dos grafos minimo, de lo contrario se omitira." )
    opcionMenu = input('Ingrese una opcion>> ') 
    if (opcionMenu == '1'):
        validacion = 1 # Variable en la cual valida si el usuario ingresó correctamente o no
        while(validacion == 1):
          validacion2 = 1 # Variable en la cual valida si se ha detectado un error en el ingreso de datos
          Grafo.reset()
          vertices = input('Ingrese vertices separados por espacio>> ')
          vertices = vertices.split(" ") # a b c => [a, b, c]
          for vertice in vertices:
              Grafo.addVertice(vertice)
          aristas_peso = input('Ingrese aristas y su peso. Ej: a,b,2 b,c,3>> ')
          aristas_peso = aristas_peso.split(" ")
          for a in aristas_peso:
            a = a.split(",")
            if(len(a)==3):
              if(Grafo.comprobacion_vertice(a[0]) and Grafo.comprobacion_vertice(a[1])):
                if(Grafo.comprobacion_tipo(a[2])):
                  Grafo.addArista(a[0], a[1], a[2])  #Si en caso que todo corre sin ningun error
                  Grafo.addAristaList(a)
                else:
                   validacion2 = 2 #En caso de que el usuario comete un error
              else:
                validacion2 = 2 #En caso de que el usuario comete un error
            else:
              validacion2 = 2 #En caso de que el usuario comete un error
          if(validacion2 == 2):
            print(" Mal ingreso de datos, revisa y vuelve a intentar ...")
          else:
            validacion = 2
            Grafos.AddGrafo(Grafo.vertices, Grafo.aristas)
            print("Datos ingresados correctamente, se tomará en cuenta el grafo ingresado.")
        input("Presione ENTER para continuar...")
        os.system("clear")
        
    elif (opcionMenu == '2' and Grafos.cantidad != 0):
        Grafo.imprimir_matriz(Grafo.matriz)
        input("Presione ENTER para continuar...")
        os.system("clear")

    elif (opcionMenu == '3' and Grafos.cantidad != 0):
        print("Cantidad de vertices: ", len(Grafo.vertices))
        print("Cantidad de aristas: ", len(Grafo.aristas))
        print(Grafo.vertices)
        print(Grafo.aristas)
        input("Presione ENTER para continuar...")
        os.system("clear")

    elif (opcionMenu == '4' and Grafos.cantidad != 0):
        if (Grafo.isConexo()):
            print("1) El grafo es conexo.")
        else:
            print("1) El grafo NO es conexo.")
        if(Grafo.ciclico()):
          print("2) El grafo es ciclico.")
        else:
          print("2) El grafo NO es ciclico.")
        if(Grafo.camino_euleriano()):
          print("3) El grafo es euleriano.")
        else:
          print("4) El grafo NO es euleriano.")
        input("Presione ENTER para continuar...")
        os.system("clear")
        
    elif(opcionMenu == '5' and Grafos.cantidad != 0):
        caminos = input("Ingrese el largo que desea ver: ")
        print("Caminos de largo " + str(caminos))
        Grafo.Caminos(int(caminos))
        input("Presione ENTER para continuar...")
        os.system("clear")
        
    elif(opcionMenu == '6' and Grafos.cantidad != 0):
        validacion = 1 # Variable en la cual valida si el usuario ingresó correctamente o no
        while(validacion == 1):
          vertice_inicial = input("Ingrese el vertice que quieras iniciar (que sea existente): ")
          if(Grafo.comprobacion_vertice(vertice_inicial)):
              validacion = 2
          else:
            print("Mal ingreso de vertice ya que no se encuentra en el grafo, vuelve a ingresar")
        Grafo.dijkstra(vertice_inicial)
        input("Presione ENTER para continuar...")
        os.system("clear")
    
    elif (opcionMenu == '7' and Grafos.cantidad != 0): #Isomorfismo
        if(Grafos.cantidad > 1):
            validacion7 = 0
            while(validacion7 == 0):
                print("Está registrado un total de ", Grafos.cantidad, " grafos, considere el orden de los grafos ingresados, donde este ultimo valor representa la ultima posicion.")
                X = int(input("Ingrese la posicion del primer grafo: "))
                Y = int(input("Ingrese la posicion del segundo grafo: "))
                if(Grafos.ValidarPosicion(X) and Grafos.ValidarPosicion(Y)):
                    validacion7 = 1
                else:
                    print("Error, vuelve a ingresar nuevamente.")
            vertices1 = len(Grafos.verticesGrafos[X-1])
            vertices2 = len(Grafos.verticesGrafos[Y-1])
            aristas1 = len(Grafos.aristasGrafos[X-1])
            aristas2 = len(Grafos.aristasGrafos[Y-1])
            GradoGrafo1 = (2 * aristas1)
            GradoGrafo2 = (2 * aristas2)
            if (vertices1 == vertices2 and aristas1 == aristas2 and GradoGrafo1 == GradoGrafo2):
                print("Los grafos ingresados son isomorfos")
            else:
                print("Los grafos ingresados no corresponden a grafos isomorfos")
        else:
            print("Usted solo ingresó un grafo, se necesita ingresar otro grafo adicional al programa.")
        input("Presione ENTER para continuar...")
        os.system("clear")
    
    elif (opcionMenu == '8'): #Para resetear todos los grafos
        Grafo.reset()
        Grafos.reset()
        print("RESETEADO, todos los grafos eliminados.")
        input("Presione ENTER para continuar...")
        os.system("clear")

    elif (opcionMenu == '9' and Grafos.cantidad != 0):
        validacion9 = 0
        while(validacion9 == 0):
          print("Elige un grafo para ser ingresado en la opción 2, 3, 4, 5, 6")
          print("Está registrado un total de ", Grafos.cantidad, " grafos, considere el orden de los grafos ingresados, donde este ultimo valor representa la ultima posicion.")
          X = int(input("Ingrese la posicion del grafo registrado que quieras usar: "))
          if(Grafos.ValidarPosicion(X)):
            validacion9 = 1
          else:
            print("Error, vuelve a ingresar nuevamente.")
        Grafo.reset()
        vertices = Grafos.verticesGrafos[X-1]
        aristas = Grafos.aristasGrafos[X-1]
        for vertice in vertices:
           Grafo.addVertice(vertice) 
        for a in aristas: # Aristas del siguiente formato: [[a, b, 2], [a, c, 4]]
           Grafo.addAristaList(a)
           Grafo.addArista(a[0], a[1], a[2])
        input("Presione ENTER para continuar...")
        os.system("clear")
    
    elif (opcionMenu == '10' and Grafos.cantidad != 0):
      verticeP = Grafo.vertices
      aristasP = Grafo.aristas
      G = nx.DiGraph()
      G.add_nodes_from(verticeP)
      for ar in aristasP:
        G.add_edge(ar[0], ar[1], capacity=int(ar[2]))
      IsVerticeV = 0
      while(IsVerticeV == 0):
        conta = 0
        print("Los vertices que tiene este grafo son: ", verticeP)
        x = input("Ingrese el nodo de origen: ")
        y = input("Ingrese el nodo final: ")
        for vert in verticeP:
          if(x == vert):
            conta += 1
          if(y == vert):
            conta += 1
        if(conta == 2):
          IsVerticeV = 1
        else:
          print("Uno o dos de los vertices no se encuentran en este grafo, vuelve a ingresar.")
      flujo_valor, flujo_dic = nx.maximum_flow(G, x, y)
      print("Valor del flujo máximo: ", flujo_valor)
      print("Detalles del flujo: ", flujo_dic)
      input("Presione ENTER para terminar...")
    
    elif(opcionMenu == '11' and Grafos.cantidad != 0):
      Gr=nx.Graph()
      colors = ['Rojo', 'Azul', 'Verde', 'Amarillo',  'Negro', 'Rosado', 'Naranjo', 'Blanco', 'Gris', 'Morado', 'Cafe', 'Azul marino']
      Gr.add_nodes_from(Grafo.vertices)
      Gr.add_weighted_edges_from(Grafo.aristas)
      colors_of_nodes={}
      def coloring(node, color):
        for neighbor in Gr.neighbors(node):
          color_of_neighbor = colors_of_nodes.get(neighbor, None)
          if color_of_neighbor == color:
            return False
          return True

      def get_color_for_node(node):
        for color in colors:
          if coloring(node, color):
            return color

      def numero_cromatico(Gr):
        for node in Gr.nodes():
          colors_of_nodes[node] = get_color_for_node(node)
        print(colors_of_nodes)
      numero_cromatico(Gr)
      input("Presione ENTER para continuar...")
      os.system("clear")

    elif (opcionMenu == '12' and Grafos.cantidad != 0):
        if(Grafo.isConexo()):
            aplicacion_kruskal()
        else:
            print("El grafo NO es conexo, por lo que no servirá para aplicar el algoritmo Kruskal.")
        input("Presione ENTER para terminar...")
        os.system("clear")

    elif (opcionMenu == '13' and Grafos.cantidad != 0):
        if(Grafo.isConexo()):
            x = {}
            for v in Grafo.vertices:
                adjacencia = []
                for a in Grafo.aristas:
                    if(v==a[0]):
                        adjacencia.append((a[1], a[2]))
                    elif(v==a[1]):
                        adjacencia.append((a[0], a[2]))
                x[v] = adjacencia
            # Se elige un nodo existente de acuerdo a lo que ingrese el usuario
            validacionVertice = 0
            while(validacionVertice == 0):
                print("El grafo que se está viendo contiene los siguientes vertices: ", Grafo.vertices)
                nodo = input("\nIngrese un vertice (nodo) para aplicar al algoritmo Prim: ")
                for v in Grafo.vertices:
                    if(v==nodo):
                        validacionVertice = 1
                        break
                if(validacionVertice == 0):
                    print("Usted no ingresó correctamente el vertice, vuelve a intentarlo...")
            Prim(x, nodo)    
        else:
            print("El grafo NO es conexo, por lo que no servirá para aplicar el algoritmo PRIM.")
        input("Presione ENTER para terminar...")
        os.system("clear")

    elif (opcionMenu == '14'):
        print("Gracias por utilizar el programa ^_^")
        input("Presione ENTER para terminar...")
        break 
    
    else:
        if(Grafos.cantidad == 0):
            print("Para proceder con otras opciones, debe ingresar un grafo")
        else:
            print("No has ingresado correctamente las opciones, vuleve a intentarlo")
        input("Presione ENTER para terminar...")
        os.system("clear")
