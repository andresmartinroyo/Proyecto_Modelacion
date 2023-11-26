from functions.functions import *

def main():
    javier_graph = create_graph("bd/javier_adj_list.csv")
    andreina_graph = create_graph("bd/andreina_adj_list.csv")
    j_path_1, j_cost_1, a_path_1, a_cost_1 = compare_paths(javier_graph,andreina_graph,5)
    print(j_path_1)
    print(a_path_1)
    j_path, a_path = find_quickest_paths(javier_graph,andreina_graph,0)
    print(j_path)
    print(a_path)



if __name__ == '__main__':
    main()
