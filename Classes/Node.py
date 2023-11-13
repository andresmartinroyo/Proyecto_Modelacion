class Node:
    
    """
    Este es el constructor de Node. 
    name: Nombre del Nodo, en este caso la intersección
    position_adj_list: En la matriz adjunta del grado, este nodo tendrá la [postion_adj_list // 6][position_adj_list mod 6]
    """
    def __init__(self, name, position_adj_list):
        self.name = name
        self.postion_adj_list = int(position_adj_list)