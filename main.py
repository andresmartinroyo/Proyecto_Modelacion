from functions.functions import *
from interface.interface import  start

def main():
    javier_graph = create_graph("bd/javier_adj_list.csv")
    andreina_graph = create_graph("bd/andreina_adj_list.csv")
    j_path, a_path = find_quickest_paths(javier_graph,andreina_graph,33)
    print(j_path)
    print(a_path)
    #start(javier_graph)



if __name__ == '__main__':
    main()
