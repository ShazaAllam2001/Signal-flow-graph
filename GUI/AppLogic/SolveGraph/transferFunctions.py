import networkx as nx

from AppLogic.SolveGraph.forwardPaths import get_fwdPath_gain


def calculate_transfer_function(graph: nx.DiGraph, deltas, delta, fwd_paths):
    summation = 0
    for index in range(len(fwd_paths)):
        p_i = get_fwdPath_gain(graph, fwd_paths[index])
        summation += p_i * deltas[index]
    
    return summation / delta
