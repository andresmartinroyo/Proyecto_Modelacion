class Node:
    
    """
    Este es el constructor de Node. 
    name: Nombre del Nodo, en este caso la intersección
    postion_adj_list: es la posicion de la fila en la matriz de adyacencia
    """
    def __init__(self, name, position_adj_list):
        self.name = name
        self.postion_adj_list = int(position_adj_list)