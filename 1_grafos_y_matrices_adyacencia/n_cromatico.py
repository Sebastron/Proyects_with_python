import networkx as nx 

colores = ('Rojo', 'Azul', 'Verde', 'Amarillo',  'Negro', 'Rosado', 'Naranjo', 'Blanco', 'Gris', 'Morado', 'Cafe', 'Azul marino')

def colorear(node, color, Gr, colores_de_nodos):
    for neighbor in Gr.neighbors(node):
        color_of_neighbor = colores_de_nodos.get(neighbor, None)
        if color_of_neighbor == color:
            return False
        return True

def get_color(node, Gr, colores_de_nodos):
    for color in colores:
        if colorear(node, color, Gr, colores_de_nodos):
            return color

def numero_cromatico(Gr, colores_de_nodos={}):
    for node in Gr.nodes():
        colores_de_nodos[node] = get_color(node, Gr, colores_de_nodos)
    print(colores_de_nodos)

def cromatico(Grafo):
      Gr=nx.Graph()
      Gr.add_nodes_from(Grafo.vertices)
      Gr.add_weighted_edges_from(Grafo.aristas)
      numero_cromatico(Gr)