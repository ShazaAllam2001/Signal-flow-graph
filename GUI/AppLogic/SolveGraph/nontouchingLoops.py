import networkx as nx
import itertools

def get_nonTouching_loops(loop_paths):
    r = 2 # number of non touching loops
    nonTouching_exits = False
    nonTouching_paths = []
    while True:
        paths = []
        combinations = itertools.combinations(loop_paths, r)
        for combination in combinations:
            areNonTouching = True
            for index in range(r-1):
                G1 = nx.path_graph(combination[index], create_using=nx.DiGraph)
                G2 = nx.path_graph(combination[(index+1) % (r+1)], create_using=nx.DiGraph)
                G: nx.DiGraph = nx.intersection(G1, G2)
                if len(G.nodes) != 0:
                    areNonTouching = False
                    break
            if areNonTouching:
                nonTouching_exits = True
                paths.append(combination) 
        if nonTouching_exits:
            r += 1
            nonTouching_exits = False
            nonTouching_paths.append(paths)
        else:
            break
    return nonTouching_paths