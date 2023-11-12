import csv
from Classes.Graph import Graph
from Classes.Node import Node


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
        graph.add_edge(edge[0],edge[1],edge[2])
    
    return graph
