from Classes.Node import Node

class Graph:

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        
    def add_node(self, node : Node):
        if node not in self.nodes:
            self.nodes[node.postion_adj_list] = node.name
        
    """
    Esta funcion agregara un arco al grafo, verificando que ambos nodos existan
    """
    def add_edge(self, origin, destination, weight):
        if origin in self.nodes and destination in self.nodes:
            if self.edges.get(origin) == None:
                self.edges[origin] = []
            self.edges[origin].append([destination,weight])