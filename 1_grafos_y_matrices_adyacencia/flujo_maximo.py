import networkx as nx      

def flujo_maximo(Grafo):
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