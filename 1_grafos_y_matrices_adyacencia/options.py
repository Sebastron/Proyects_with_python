import os
import classGrafoN
import classGrafoWithMetod
import flujo_maximo as fm
import n_cromatico as nc
import kruskal as kr
import prim as pm

print('MATRICES DE ADYACENCIA DE GRAFOS\n')

def menu(GN):

    print(
        f"Actualmente, tienen ingresado", GN.cantidad, "grafos, para la opcion de isomorfismo se requiere dos grafos minimo, de lo contrario se omitira.\n"
        f" -------------------------------\n"
        f"1. Ingresar Grafo\n"
        f"2. Mostrar Matriz de Adyacencia\n"
        f"3. Imprimir cantidad de vertices y aristas\n"
        f"4. Tipo de grafo (conexo, ciclico, euleriano)\n"
        f"5. Caminos\n"
        f"6. Dijkstra\n"
        f"7. Isomorfismo, se requiere 2 grafos ingresado, de lo contrario se omitira\n"
        f"8. Resetear todos los grafos\n"
        f"9. Eligir un grafo registrado para opciones 2, 3, 4, 5 y 6\n"
        f"10. Flujo Maximo\n"
        f"11. Numero cromatico y coloreo\n"
        f"12. Arbol Kruskal, aplicable solo grafo conexo\n"
        f"13. Arbol Prim, aplicable solo grafo conexo\n"
        f"14. Salir\n"
        f" ------------------------------- \n")
    n = input('Ingrese una opcion>> ') 
    return n


def option(Grafo, Grafos):
    while True:
        opcionMenu = menu(Grafos)
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
                    print("Datos ingresados correctamente, se tomara en cuenta el grafo ingresado.")
        
        elif (opcionMenu == '2' and Grafos.cantidad != 0):
            Grafo.imprimir_matriz(Grafo.matriz)

        elif (opcionMenu == '3' and Grafos.cantidad != 0):
            print("Cantidad de vertices: ", len(Grafo.vertices))
            print("Cantidad de aristas: ", len(Grafo.aristas))
            print(Grafo.vertices)
            print(Grafo.aristas)

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
        
        elif(opcionMenu == '5' and Grafos.cantidad != 0):
            caminos = input("Ingrese el largo que desea ver: ")
            print("Caminos de largo " + str(caminos))
            Grafo.Caminos(int(caminos))
        
        elif(opcionMenu == '6' and Grafos.cantidad != 0):
            validacion = 1 # Variable en la cual valida si el usuario ingresó correctamente o no
            while(validacion == 1):
                vertice_inicial = input("Ingrese el vertice que quieras iniciar (que sea existente): ")
                if(Grafo.comprobacion_vertice(vertice_inicial)):
                  validacion = 2
                else:
                    print("Mal ingreso de vertice ya que no se encuentra en el grafo, vuelve a ingresar")
            Grafo.dijkstra(vertice_inicial)
    
        elif (opcionMenu == '7' and Grafos.cantidad != 0): #Isomorfismo
            if(Grafos.cantidad > 1):
                validacion7 = 0
                while(validacion7 == 0):
                    print("Esta registrado un total de ", Grafos.cantidad, " grafos, considere el orden de los grafos ingresados, donde este ultimo valor representa la ultima posicion.")
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
                print("Usted solo ingreso un grafo, se necesita ingresar otro grafo adicional al programa.")
    
        elif (opcionMenu == '8'): #Para resetear todos los grafos
            Grafo.reset()
            Grafos.reset()
            print("RESETEADO, todos los grafos eliminados.")

        elif (opcionMenu == '9' and Grafos.cantidad != 0):
            validacion9 = 0
            while(validacion9 == 0):
                print("Elige un grafo para ser ingresado en la opcion 2, 3, 4, 5, 6")
                print("Esta registrado un total de ", Grafos.cantidad, " grafos, considere el orden de los grafos ingresados, donde este ultimo valor representa la ultima posicion.")
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
    
        elif (opcionMenu == '10' and Grafos.cantidad != 0):
            fm.flujo_maximo(Grafo)
    
        elif(opcionMenu == '11' and Grafos.cantidad != 0):
            nc.cromatico(Grafo)

        elif (opcionMenu == '12' and Grafos.cantidad != 0):
            if(Grafo.isConexo()):
                kr.aplicacion_kruskal(Grafo)
            else:
                print("El grafo NO es conexo, por lo que no servira para aplicar el algoritmo Kruskal.")

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
                    print("El grafo que se esta viendo contiene los siguientes vertices: ", Grafo.vertices)
                    nodo = input("\nIngrese un vertice (nodo) para aplicar al algoritmo Prim: ")
                    for v in Grafo.vertices:
                        if(v==nodo):
                            validacionVertice = 1
                            break
                    if(validacionVertice == 0):
                        print("Usted no ingreso correctamente el vertice, vuelve a intentarlo...")
                pm.Prim(x, nodo)    
            else:
                print("El grafo NO es conexo, por lo que no servira para aplicar el algoritmo PRIM.")

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