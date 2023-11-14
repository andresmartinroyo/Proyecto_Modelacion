from Classes.Node import Node

class Graph:

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.adjacency_matrix = None
        self.dijkstras_matrix = None
        
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

    def copy_graph(self):
        copy = Graph()
        copy.nodes = self.nodes
        for i in range(0,len(copy.nodes)):
            copy.edges[i] = []
        for node, arcs in self.edges.items():
            for arc in arcs:
                copy.edges[node].append([arc[0],arc[1]])
        return copy