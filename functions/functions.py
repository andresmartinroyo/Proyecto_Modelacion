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
    
def creat_original_graph(graph_1, graph_2):
    nodes_list = read_csv("bd/lista_de_nodos.csv")
    graph = Graph()
    for node in nodes_list:
        new_node = Node(node[0],node[1])
        graph.add_node(new_node)

    edges_list = read_csv(graph_1)
    for edge in edges_list:
        graph.add_edge(int(edge[0]),int(edge[1]),int(edge[2]))
        
    edges2_list = read_csv(graph_2)
    for edge2 in edges2_list:
        graph.add_edge2(int(edge2[0]),int(edge2[1]),int(edge2[2]))

    return graph
    

    
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
        path.append([predecessors[current_node],current_node])
        current_node = predecessors[current_node]
    path.reverse()
    return path, distances[destination]


def compare_paths(j_graph : Graph, a_graph : Graph, destination):
    j_path, j_cost = dijkstra(j_graph, 7, destination)
    a_path, a_cost = dijkstra(a_graph,20, destination)
    intersection = intersect(j_path,a_path)
    if len(intersection) == 0:
        return j_path, j_cost, a_path, a_cost
    else:
        if j_cost < a_cost:
            j_graph_copy = j_graph.copy_graph()
            for component in intersection:
                for arcs in j_graph_copy.edges[component[0]]:
                    if component[1] == arcs[0]:
                        arcs[1] = float("inf")
            return compare_paths(j_graph_copy,a_graph,destination)
        else :
            a_graph_copy = a_graph.copy_graph()
            for component in intersection:
                for arcs in a_graph_copy.edges[component[0]]:
                    if component[1] == arcs[0]:
                        arcs[1] = float("inf")
            return compare_paths(j_graph,a_graph_copy,destination)
        
def intersect(list1 : list, list2: list):
    intersection = []
    for element1 in list1:
        for element2 in list2:
            if element1[0] == element2[0] and element1[1] == element2[1]:
                intersection.append(element2)
    return intersection
