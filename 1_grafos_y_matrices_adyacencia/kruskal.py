import classGrafoWithMetod

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
    Ordenada = [(c,a,b) for a,b,c in Ordenada]
    # Se recorre la lista de aristas que están ordenadas
    for Dato in Ordenada:
        peso, u, v = Dato
        # Se verifica que ambos nodos sean distintos
        if Find_set(u, Nodo) != Find_set(v, Nodo):
            # Se almacena al arista de menor peso
            resultante.append(Dato)
            resultante = [(a,b,c) for c,a,b in resultante]
            resultante = [(c,a,b) for a,b,c in resultante]
            cont+=1
            Union(u, v, Ordenada, Nodo)
    return resultante

def aplicacion_kruskal(Grafo):
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