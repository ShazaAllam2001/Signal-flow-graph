import networkx as nx

from AppLogic.SolveGraph.forwardPaths import get_total_gain

def generate_all_loops(graph: nx.DiGraph):
    return nx.simple_cycles(graph)

def get_loops_gains(graph: nx.DiGraph, cycle):
    gains = []
    length = len(cycle) 
    for i in range(length):
        edgeData = graph.get_edge_data(cycle[i], cycle[(i + 1) % length])
        gains.append(edgeData['weight'])
    return get_total_gain(gains)
