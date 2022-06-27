# Grafos y Matrices de adyacencia

## Descripción 🚀

El proyecto consta de estudio sobre [Grafos](https://www.unipamplona.edu.co/unipamplona/portalIG/home_23/recursos/general/11072012/grafo3.pdf) y 
[Matrices de adyacencia](https://www.ecured.cu/Matriz_de_adyacencia), cuyo programa implementado, cuenta con una serie de opciones, donde estos se mencionan a continuación:

* Mostrar por pantalla la matriz de adyacencia.
* Imprimir cantidad de vertices y aristas al grafo ingresado o seleccionado.
* Mostrar por pantalla si el grafo es [conexo](https://www.ecured.cu/Grafo_conexo), [ciclico](https://es-academic.com/dic.nsf/eswiki/262725#Propiedades) y/o [eureliano](https://www.ecured.cu/Grafo_euleriano).
* Ingresar el largo que quiera ver y mostrar las cantidades de camino de cada vértice (nodo).
* Aplicar el algoritmo [Dijkstra](https://www.ecured.cu/Algoritmo_de_Dijkstra) para encontrar el camino más corto, según el vértice elegido.
* Con dos grafos ingresados y seleccionados, se compara si son [isomorfismos](https://es-academic.com/dic.nsf/eswiki/620374).
* Determinar el [flujo máximo](http://dis.um.es/~ginesgm/files/doc/aed/sec5.6.3-5.8.pdf) del grafo, según los dos vértices (inicial y final)
* Mostrar por pantalla el [número cromatico y coloración](http://www.matetam.com/glosario/definicion/numero-cromatico) de un grafo, donde muestra los colores que se asignan en cada vértice
* Aplicación del algoritmo [Kruskal](https://nodo.ugto.mx/wp-content/uploads/2018/08/Kruskal.pdf) de un grafo, aplicable solo de tipo conexo.
* Aplicación de otro algoritmo [Prim](https://www.ecured.cu/Algoritmo_de_Prim) en un grafo, aplicable solo de tipo conexo.

Al ingresar el último grafo en el programa correctamente, queda seleccionado para aplicar distintas opciones de forma automática. Sin embargo, al almacenar los otros grafos según el orden que se ha ingresado (1 a N), cuenta con una opción de elegir uno de ellos. Para la opción del menú sobre "Isomorfismo", puede elegir dos grafos ingresados al programa, considerando el dicho orden mencionado anteriormente. En estricto rigor, también cuenta la opción de eliminar todos los grafos almacenados. Para ingresar un grafo correctamente, debe escribir por pantalla los vertices en la forma "v1 v2 vn" y aristas "v1,v2,X v2,vn,Y vn,v1,Z", donde "v" representa el vertice y las otras variables "X, Y y Z" representan el peso de aristas.

## Requisitos 📋

* Tener instalado la librería numpy:
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    pip install numpy
<!--endsec-->

* Tener instalado la librería networkx:
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    pip install networkx
<!--endsec-->

* En caso de requerir alguna actualización de Python
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    python -m pip install --upgrade pip
<!--endsec-->

## Ejecución del programa 🔧

Para ejecutarlo por terminal, debe posicionarse en esta carpeta e ingresar el siguiente comando
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    python main.py
<!--endsec-->
