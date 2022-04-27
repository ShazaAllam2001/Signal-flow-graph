import networkx as nx
from forwardPaths import get_fwdPaths_gains
from deltaCalculations import calculate_delta_i
from deltaCalculations import calculate_delta


def calculate_transfer_function(graph: nx.DiGraph, paths, loops, non_touching_loops):
    summation = 0
    for path in paths:
        p_i = get_fwdPaths_gains(graph, path)
        delta_i = calculate_delta_i(graph, path, loops, non_touching_loops)
        summation += p_i * delta_i
    delta = calculate_delta(graph, loops, non_touching_loops)
    return summation / delta
