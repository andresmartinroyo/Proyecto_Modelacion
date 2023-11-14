from functions.functions import *

def main():
    javier_graph = create_graph("bd/javier_adj_list.csv")
    andreina_graph = create_graph("bd/andreina_adj_list.csv")
    j_path, j_cost, a_path, a_cost = compare_paths(javier_graph,andreina_graph,35)
    print(j_path)
    print(a_path)


if __name__ == '__main__':
    main()
