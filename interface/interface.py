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
    global interface, right_frame, left_frame
   # Crear la ventana principal
    interface = tk.Tk()
    interface.title("MetroTravel")
    interface.configure(bg="orange")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12), background="orange")
    style.configure("TButton", font=("Arial", 12))
    style.configure("TFrame", background="orange")

    # Lado izquierdo
    left_frame = ttk.Frame(interface, style="TFrame")
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Título centrado
    title = ttk.Label(left_frame, text="Bienvenido a MetroTravel",
                      font=("Arial", 20), background="orange")
    title.grid(row=0, column=0, columnspan=4, pady=10)

    originsLabel = ttk.Label(
        left_frame, text="País de Origen:", style="TLabel")
    originsLabel.grid(row=1, column=0, padx=10, sticky="w")
    origins = originsList(graph)
    origin = ttk.Combobox(left_frame, values=origins)
    origin.grid(row=2, column=0, padx=10)

    destinationLabel = ttk.Label(
        left_frame, text="País de Destino:", style="TLabel")
    destinationLabel.grid(row=1, column=1, padx=10, sticky="w")
    destinations = destinationsList(graph)
    destination = ttk.Combobox(left_frame, values=destinations)
    destination.grid(row=2, column=1, padx=10, sticky="w")

    visaLabel = ttk.Label(
        left_frame, text="¿Cuenta con Visa?:", style="TLabel")
    visaLabel.grid(row=1, column=2, padx=10, sticky="w")
    visa = ttk.Combobox(left_frame, values=["Si", "No"], state="readonly")
    visa.grid(row=2, column=2, padx=10)

    pathLabel = ttk.Label(left_frame, text="Tipo de ruta:", style="TLabel")
    pathLabel.grid(row=1, column=3, padx=10, sticky="w")
    pathType = ttk.Combobox(left_frame, values=[
                            "Ruta más barata", "Ruta con menos paradas"], state="readonly")
    pathType.grid(row=2, column=3, padx=10)

   # travel = ttk.Button(left_frame, text="Buscar vuelos", command=lambda: printRoute(
    #    graph, origin, destination, visa, pathType), style="TButton")
    #travel.grid(row=3, column=0, columnspan=4, pady=20)
    
    information = ttk.Label(left_frame, text="¡Importante!", font=("Arial", 14), background="orange")
    information.grid(row=6, column=0, columnspan=4, pady=5)
    
    information1 = ttk.Label(left_frame, text="Los países en rojo requieren visa.", font=("Arial", 14), background="orange")
    information1.grid(row=7, column=0, columnspan=4, pady=5)
    
    # Lado derecho
    right_frame = ttk.Frame(interface)
    right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    drawGraph(graph)

    interface.mainloop()

def drawGraph(graph: Graph):
    g = nx.Graph()
    nodeColors = {}
    # Agregar nodos y aristas al grafo
    for node, neighbors in graph.edges.items():
        #if (graph.nodes[node].visaRequired):
            #nodeColors[node] = 'red'
        #else:
            #nodeColors[node] = 'yellow'
        for neighbor, cost in neighbors:
            g.add_edge(node, neighbor, weight=cost)

    # Crear un layout para el grafo
    posNX = nx.spring_layout(g, seed=900)

    # Agregamos los colores
    #nodes_colorsNX = [nodeColors[node]
    #                  for node in g.nodes()]

    plt.clf()

    # Dibujar el grafo
    #nx.draw(g, pos=posNX, with_labels=True, node_size=600, node_color=nodes_colorsNX,
    #        font_size=10, width=1, alpha=0.7)

    # Agregar el canvas al lado derecho
    canvas = FigureCanvasTkAgg(plt.gcf(), master=right_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def originsList(graph: Graph):
    global origins
    origins = []
    for node, neighbors in graph.edges.items():
        origins.append(node)
    return origins


def destinationsList(graph: Graph):
    global destinations
    destinations = []
    for node, neighbors in graph.edges.items():
        destinations.append(node)
    return destinations