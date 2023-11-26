import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Classes.Graph import Graph
#from scripts.csv import * 
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def start(graph: Graph):
    global interface, frame
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

    # Título centrado
    title = ttk.Label(frame, text="Ayuda a Javier y Andreina a poder juntarse!",
                      font=("Arial", 20), background="purple")
    title.grid(row=0, column=0, columnspan=4, pady=10)

    originsLabel = ttk.Label(frame, text="Destino:", style="TLabel")
    originsLabel.grid(row=1, column=0, padx=10, sticky="w")
    origins = originsList(graph)
    origin = ttk.Combobox(frame, values=origins)
    origin.grid(row=1, column=0, padx=80)

   # travel = ttk.Button(left_frame, text="Buscar vuelos", command=lambda: printRoute(
    #    graph, origin, destination, visa, pathType), style="TButton")
    #travel.grid(row=3, column=0, columnspan=4, pady=20)
    
    # Lado derecho
    frame = ttk.Frame(interface)
    frame.grid(row=10, column=0, padx=10, pady=10, sticky="nsew")

    drawGraph(graph)

    interface.mainloop()

def drawGraph(graph: Graph):
    g = nx.Graph()
    nodeColors = {}
    # Agregar nodos y aristas al grafo
    for node, neighbors in graph.edges.items():
        nodeColors[graph.nodes[node]] = 'red'
        #if (graph.nodes[node].visaRequired):
            #nodeColors[node] = 'red'
        #else:
            #nodeColors[node] = 'yellow'
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
    canvas = FigureCanvasTkAgg(plt.gcf(), master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def originsList(graph: Graph):
    global origins
    origins = []
    for node in graph.nodes.items():
        origins.append(node[-1])
    return origins


def destinationsList(graph: Graph):
    global destinations
    destinations = []
    for node, neighbors in graph.edges.items():
        destinations.append(node)
    return destinations