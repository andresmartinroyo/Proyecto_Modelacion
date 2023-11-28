import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Classes.Graph import Graph
#from scripts.csv import * 
from functions.functions import *
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def start(graph: Graph):
    global interface, frame, graphFrame
   # Crear la ventana principal
    interface = tk.Tk()
    interface.title("Camino del Amor")
    interface.configure(bg="purple")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 18), background="purple")
    style.configure("TButton", font=("Arial", 18))
    style.configure("TFrame", background="purple")

    # Lado izquierdo
    frame = ttk.Frame(interface, style="TFrame")
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    title = ttk.Label(frame, text="Camino del amor",
                      font=("Arial", 24), background="purple")
    title.grid(row=0, column=0, columnspan=12, pady=10)

    # Título centrado
    title = ttk.Label(frame, text="Ayuda a Javier y Andreina a poder juntarse!",
                      font=("Arial", 14), background="purple")
    title.grid(row=1, column=0, columnspan=4, pady=10)

    originsLabel = ttk.Label(frame, text="Destino:", style="TLabel")
    originsLabel.grid(row=2, column=0, padx=0, sticky="w")
    origins = originsList(graph)
    origin = ttk.Combobox(frame, values=origins)
    origin.grid(row=2, column=0, padx=90)

    travel = ttk.Button(frame, text="Buscar", command=lambda: printRoute(
        graph, origin), style="TButton")
    travel.grid(row=2, column=4, columnspan=4)

    graphFrame = ttk.Frame(interface)
    graphFrame.grid(row=15, column=0, padx=10, pady=10, sticky="nsew")

    drawGraph(graph)

    interface.mainloop()

def drawGraph(graph: Graph):
    g = nx.Graph()
    nodeColors = {}
    # Agregar nodos y aristas al grafo
    for node, neighbors in graph.edges.items():
        
        if (graph.nodes[node] == 'A' or graph.nodes[node] == 'J'):
            nodeColors[graph.nodes[node]] = 'green'
        elif (graph.nodes[node] == 'BLP' or graph.nodes[node] == 'CMR' or graph.nodes[node] == 'DTD' or graph.nodes[node] == 'CS'):
            nodeColors[graph.nodes[node]] = 'blue'
        else:
            nodeColors[graph.nodes[node]] = 'red'
            
        for neighbor, cost in neighbors:
            g.add_edge(graph.nodes[node], graph.nodes[neighbor] , weight=cost)

    # Crear un layout para el grafo
    posNX = nx.spring_layout(g, seed=900)
    # Agregamos los colores
    nodes_colorsNX = [nodeColors[node]
                      for node in g.nodes()]

    plt.clf()

    # Dibujar el grafo
    nx.draw(g, pos=posNX, with_labels=True, node_size=600, node_color=nodes_colorsNX,
            font_size=10, width=1, alpha=0.7)

    # Agregar el canvas al lado derecho
    canvas = FigureCanvasTkAgg(plt.gcf(), master=graphFrame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def originsList(graph: Graph):
    global origins
    origins = ['Discoteca The Darkness','Bar La Pasión','Cervecería Mi Rolita','Café Sensación']
    return origins

def clearRows(list):
    for column in list:
        widgets = frame.grid_slaves(column=column)
        for widget in widgets:
            widget.grid_forget()
    

    for widget in graphFrame.winfo_children():
        widget.destroy()

def printRoute(graph, destination):
    clearRows([4, 5, 6, 7, 8])
    if (destination.get() != ""):

        destinationT = ""
        graphFrame = ttk.Frame(interface)
    
        try:
            #shortest_distance, shortest_path = graph.findShortestStopPath(
                #startNode, end_node, hasVisa)

            if(destination.get() == 'Discoteca The Darkness'):
                destinationT = 31
            elif(destination.get() == 'Bar La Pasión'):
                destinationT = 10
            elif(destination.get() == 'Cervecería Mi Rolita'):
                destinationT = 33
            elif(destination.get() == 'Café Sensación'):
                destinationT = 35
            
            javier_graph = create_graph("bd/javier_adj_list.csv")
            andreina_graph = create_graph("bd/andreina_adj_list.csv")
            j_path, a_path = find_quickest_paths(javier_graph,andreina_graph,destinationT)

            min_j = j_path[-1][-1] - j_path[0][-1]
            min_a = a_path[-1][-1] - a_path[0][-1]

            for road in j_path:
                if(road[0] != None):
                    road[0] = graph.nodes[road[0]]
                else:
                    road[0] = 'J'
                road[1] = graph.nodes[road[1]]

            for road in a_path:
                if(road[0] != None):
                    road[0] = graph.nodes[road[0]]
                else:
                    road[0] = 'A'
                road[1] = graph.nodes[road[1]]

            drawGraphNX(graph, j_path, a_path, andreina_graph,min_j,min_a)
        
        except ValueError as e:
            errorDialog(e)
            print("Error")
            drawGraph(graph)
            
            style = ttk.Style()
            style.configure("TLabel", font=("Arial", 18), background="purple")
            style.configure("TButton", font=("Arial", 18))
            style.configure("TFrame", background="purple")

            # Lado izquierdo
            frame = ttk.Frame(interface, style="TFrame")
            frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

            title = ttk.Label(frame, text="Camino del amor",
                            font=("Arial", 24), background="purple")
            title.grid(row=0, column=0, columnspan=12, pady=10)

            # Título centrado
            title = ttk.Label(frame, text="Ayuda a Javier y Andreina a poder juntarse!",
                            font=("Arial", 14), background="purple")
            title.grid(row=1, column=0, columnspan=4, pady=10)

            originsLabel = ttk.Label(frame, text="Destino:", style="TLabel")
            originsLabel.grid(row=2, column=0, padx=0, sticky="w")
            origins = originsList(graph)
            origin = ttk.Combobox(frame, values=origins)
            origin.grid(row=2, column=0, padx=90)

            travel = ttk.Button(frame, text="Buscar", command=lambda: printRoute(
                graph, origin), style="TButton")
            travel.grid(row=2, column=4, columnspan=4)
    else:
        validateDialog()
        drawGraph(graph)
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 18), background="purple")
        style.configure("TButton", font=("Arial", 18))
        style.configure("TFrame", background="purple")

        # Lado izquierdo
        frame = ttk.Frame(interface, style="TFrame")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        title = ttk.Label(frame, text="Camino del amor",
                        font=("Arial", 24), background="purple")
        title.grid(row=0, column=0, columnspan=12, pady=10)

        # Título centrado
        title = ttk.Label(frame, text="Ayuda a Javier y Andreina a poder juntarse!",
                        font=("Arial", 14), background="purple")
        title.grid(row=1, column=0, columnspan=4, pady=10)

        originsLabel = ttk.Label(frame, text="Destino:", style="TLabel")
        originsLabel.grid(row=2, column=0, padx=0, sticky="w")
        origins = originsList(graph)
        origin = ttk.Combobox(frame, values=origins)
        origin.grid(row=2, column=0, padx=90)

        travel = ttk.Button(frame, text="Buscar", command=lambda: printRoute(
            graph, origin), style="TButton")
        travel.grid(row=2, column=4, columnspan=4)

def drawGraphNX(graph: Graph, shortestPath: list, shortestPath2: list, andreina_graph: Graph,min_j : int, min_a:int):
    g = nx.Graph()
    andreinaGraph = nx.Graph()

    # Agregar nodos y aristas al grafos
    for node, neighbors in graph.edges.items():
        for neighbor, cost in neighbors:
            g.add_edge(graph.nodes[node],graph.nodes[neighbor], weight=cost)

    for node, neighbors in andreina_graph.edges.items():
        for neighbor, cost in neighbors:
            andreinaGraph.add_edge(graph.nodes[node],graph.nodes[neighbor], weight=cost)

    path =[]
    adreinaPath = []

    for road in shortestPath:
        path.append(road[1])

    for road in shortestPath2:
        adreinaPath.append(road[1])

    # Crear un layout para el grafo
    posNX = nx.spring_layout(g, seed=900)

    # Diccionario para elegir el color del path tomado para el camino mas corto
    node_colors_shortestPath = {}

    # Diccionario para elegir el color de los edges tomados para el camino mas corto
    node_colors_shortestEdge = {}

    # Diccionario para agregarle le peso al camino usado
    edge_labels = {}

    # Diccionario para elegir el color del path tomado para el camino mas corto
    node_colors_shortestPath2 = {}

    # Diccionario para elegir el color de los edges tomados para el camino mas corto
    node_colors_shortestEdge2 = {}

    # Diccionario para agregarle le peso al camino usado
    edge_labels2 = {}

    # For loop para agregar los datos a cada diccionario
    for node in g.nodes():
        origNode = ''
        destNode = ''
        if (node in path):
            # Verificamos si tiene visa para pintarlo de un color u otro
            if (node == 'J'):
                node_colors_shortestPath[node] = 'green'
            elif (node == 'BLP' or node == 'CMR' or node == 'DTD' or node == 'CS'):
                node_colors_shortestPath[node] = 'blue'
            else:
                node_colors_shortestPath[node] = 'red'
            # Obtenemos la posición del nodo actual en la lista del camino
            pos = path.index(node)
            if (pos == 0):
                node_colors_shortestPath[node] = "green"
            # Se verifica si el nodo que se está revisando es el último para poder setear correctamente el nodo origen y destino
            if (pos == len(shortestPath) - 1):
                origNode = shortestPath[pos - 1]
                destNode = shortestPath[pos]
            else:
                origNode = shortestPath[pos]
                destNode = shortestPath[pos + 1]
        # En caso de que no se encuentre en el camino a seguir, el nodo y su camino se pintan de gris y se sigue continua con el siguiente nodeo del for
        else:
            node_colors_shortestPath[node] = "gray"
            node_colors_shortestEdge[node] = 'gray'
            continue
        # En caso de que node se encuentre en el camino más corto, se pinta de rojo su arista y se coloca su peso para ser visualizado
        node_colors_shortestEdge[(origNode[1], destNode[1])] = 'red'
        node_colors_shortestEdge[(destNode[1], origNode[1])] = 'red'
        
        edge_labels[(origNode[1], destNode[1])] = str(
            g[origNode[1]][destNode[1]]['weight'])

    # Colores para el grafo
    colors_shortestPath = [node_colors_shortestPath[node]
                           for node in g.nodes()]
    colors_shortestEdge = [node_colors_shortestEdge.get(
        edge, 'gray') for edge in g.edges()]

    for node in andreinaGraph.nodes():
        origNode = ''
        destNode = ''
        if (node in adreinaPath):
            # Verificamos si tiene visa para pintarlo de un color u otro
            if (node == 'A'):
                node_colors_shortestPath2[node] = 'green'
            elif (node == 'BLP' or node == 'CMR' or node == 'DTD' or node == 'CS'):
                node_colors_shortestPath2[node] = 'blue'
            else:
                node_colors_shortestPath2[node] = 'red'
            # Obtenemos la posición del nodo actual en la lista del camino
            pos = adreinaPath.index(node)
            if (pos == 0):
                node_colors_shortestPath2[node] = "green"
            # Se verifica si el nodo que se está revisando es el último para poder setear correctamente el nodo origen y destino
            if (pos == len(shortestPath2) - 1):
                origNode = shortestPath2[pos - 1]
                destNode = shortestPath2[pos]
            else:
                origNode = shortestPath2[pos]
                destNode = shortestPath2[pos + 1]
        else:
            if (node in path):
                if (node == 'J'):
                    node_colors_shortestPath2[node] = 'green'
                elif (node == 'BLP' or node == 'CMR' or node == 'DTD' or node == 'CS'):
                    node_colors_shortestPath2[node] = 'blue'
                else:
                    node_colors_shortestPath2[node] = 'red'
            else:
                node_colors_shortestPath2[node] = "gray"
                node_colors_shortestEdge2[node] = 'gray'
            continue
        # En caso de que node se encuentre en el camino más corto, se pinta de rojo su arista y se coloca su peso para ser visualizado
        node_colors_shortestEdge2[(origNode[1], destNode[1])] = 'red'
        node_colors_shortestEdge2[(destNode[1], origNode[1])] = 'red'
        
        edge_labels2[(origNode[1], destNode[1])] = str(
            andreinaGraph[origNode[1]][destNode[1]]['weight'])

    # Colores para el grafo
    colors_shortestPath = [node_colors_shortestPath[node]
                           for node in g.nodes()]
    colors_shortestEdge = [node_colors_shortestEdge.get(
        edge, 'gray') for edge in g.edges()]
    
    # Colores para el grafo
    colors_shortestPath2 = [node_colors_shortestPath2[node]
                           for node in andreinaGraph.nodes()]
    colors_shortestEdge2 = [node_colors_shortestEdge2.get(
        edge, 'gray') for edge in andreinaGraph.edges()]

    plt.clf()
    # Dibujar el grafo
    nx.draw(g, pos=posNX, with_labels=True, node_size=600, node_color=colors_shortestPath,
            font_size=10, edge_color=colors_shortestEdge, width=1, alpha=0.7)

    # Dibujar las etiquetas de las aristas
    nx.draw_networkx_edge_labels(
        g, posNX, edge_labels=edge_labels, font_color='black')
    
    # Dibujar el grafo
    nx.draw(andreinaGraph, pos=posNX, with_labels=True, node_size=600, node_color=colors_shortestPath2,
            font_size=10, edge_color=colors_shortestEdge2, width=1, alpha=0.7)

    # Dibujar las etiquetas de las aristas
    nx.draw_networkx_edge_labels(
        andreinaGraph, posNX, edge_labels=edge_labels2, font_color='black')
    
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 18), background="purple")
    style.configure("TButton", font=("Arial", 18))
    style.configure("TFrame", background="purple")

    # Lado izquierdo
    frame = ttk.Frame(interface, style="TFrame")
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    title = ttk.Label(frame, text="Camino del amor",
                      font=("Arial", 24), background="purple")
    title.grid(row=0, column=0, columnspan=12, pady=10)

    # Título centrado
    title = ttk.Label(frame, text="Ayuda a Javier y Andreina a poder juntarse!",
                      font=("Arial", 14), background="purple")
    title.grid(row=1, column=0, columnspan=4, pady=10)

    originsLabel = ttk.Label(frame, text="Destino:", style="TLabel")
    originsLabel.grid(row=2, column=0, padx=0, sticky="w")
    origins = originsList(graph)
    origin = ttk.Combobox(frame, values=origins)
    origin.grid(row=2, column=0, padx=90)

    travel = ttk.Button(frame, text="Buscar", command=lambda: printRoute(
        graph, origin), style="TButton")
    travel.grid(row=2, column=4, columnspan=4)

    destiny = shortestPath[-1][1]

    if(destiny == "DTD"):
        destiny = "Discoteca The Darkness"
    elif(destiny == "BLP"):
        destiny = "Bar La Pasión"
    elif(destiny == "CMR"):
        destiny = "Cervecería Mi Rolita"
    elif(destiny == "CS"):
        destiny = "Café Sensación"

    javierText = ttk.Label(frame, text="Javier ha tardado {} minutos en llegar a {}".format(min_j,destiny), style="TLabel", font=14)
    javierText.grid(row=3, column=0, padx=0, sticky="w")

    AndreinaText = ttk.Label(frame, text="Andreina ha tardado {} minutos en llegar a {}".format(min_a,destiny), style="TLabel", font=14)
    AndreinaText.grid(row=4, column=0, padx=0, sticky="w")

    dif = ""

    if(min_a>min_j):
        dif = "Javier tiene que esperar {} minutos".format(min_a-min_j)
    else:
        dif = "Andreina tiene que esperar {} minutos".format(min_j-min_a)

    diffText = ttk.Label(frame, text="Para llegar al mismo tiempo, {}".format(dif), style="TLabel", font=18)
    diffText.grid(row=5, column=0, padx=0, sticky="w")

    # Agregar el canvas al lado derecho
    canvas = FigureCanvasTkAgg(plt.gcf(), master=graphFrame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def errorDialog(e: str):
    messagebox.showerror("Error", e)

def validateDialog():
    messagebox.showerror("Error", "Asegurese de rellenar todos los campos.")