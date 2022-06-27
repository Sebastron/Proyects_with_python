#Aplicación del algoritmo PRIM

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