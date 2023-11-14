from functions.functions import *

def main():
    javier_graph = create_graph("bd/javier_adj_list.csv")
    andreina_graph = create_graph("bd/andreina_adj_list.csv")
    path, costo = dijkstra(javier_graph, 7,31)
    print(path)


if __name__ == '__main__':
    main()