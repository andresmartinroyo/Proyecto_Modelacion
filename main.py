from functions.functions import *
from interface.interface import  start

def main():
    GUIgraph = create_graph("bd/javier_adj_list.csv")
    start(GUIgraph)



if __name__ == '__main__':
    main()
