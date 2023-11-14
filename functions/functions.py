import csv
from Classes.Graph import Graph
from Classes.Node import Node
import heapq


def read_csv(path):
    with open(path) as f:
        reader = csv.reader(f)
        content = []
        for row in reader:
            content.append(row)
        f.close()
        return content
    
def create_graph(path):
    nodes_list = read_csv("bd/lista_de_nodos.csv")
    graph = Graph()
    for node in nodes_list:
        new_node = Node(node[0],node[1])
        graph.add_node(new_node)
    edges_list = read_csv(path)
    for edge in edges_list:
        graph.add_edge(int(edge[0]),int(edge[1]),int(edge[2]))

    """    
    graph.adjacency_matrix = graph.get_adjacency_matrix()
    graph.dijkstras_matrix = graph.get_dijkstras_matrix()
    for node in graph.adjacency_matrix:
        print(node)
    for node in graph.dijkstras_matrix:
        print(node)
    """
        
    return graph

def find_minimum(distances : list, visited : list):
    minimum = distances[0]
    index = 0
    for i in range(0,len(visited)):
        if visited[i] == 0 and minimum > distances[i]:
            minimum = distances[i]
            index = i
    return index

def find_closest_neighbors(neighbors : list):
    minimum = neighbors[0][1]
    index = 0
    for i in range(0,len(neighbors)):
        if minimum > neighbors[i][1]:
            minimum = neighbors[i][1]
            index = i
    
    return minimum, index

def dijkstra(graph: Graph, source, destination):

    # Inicialización
    visited = set()
    distances = {}
    predecessors = []
    for node in graph.nodes.keys():
        distances[node] = float("inf")
        predecessors.append(None)
    distances[source] = 0

    # Cola de prioridad
    queue = []
    heapq.heappush(queue, (distances[source], source))

    # Algoritmo de Dijkstra
    while queue:

        # Obtener el nodo con la distancia más corta
        current_distance, current_node = heapq.heappop(queue)

        # Marcar el nodo como visitado
        visited.add(current_node)

        # Actualizar las distancias de los nodos adyacentes
        for neighbor in graph.edges.get(current_node):
            if neighbor[0] not in visited:
                new_distance = current_distance + neighbor[1]
                if new_distance < distances[neighbor[0]]:
                    distances[neighbor[0]] = new_distance
                    predecessors[neighbor[0]] = current_node
                    heapq.heappush(queue, (new_distance, neighbor[0]))

    # Retornar el camino y el costo
    path = []
    current_node = destination
    while current_node != None:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()
    return path, distances[destination]