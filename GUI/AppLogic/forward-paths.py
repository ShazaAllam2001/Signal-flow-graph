import itertools
import networkx as nx
import sympy as sym


def remove_duplicates(paths):
    res = []
    for i in paths:
        if i not in res:
            res.append(i)
    return res


def gain_multiply(gains):
    return list(itertools.product(*gains))


def get_all_fwdpath_gains(fwd_paths_gain):
    total_gains = []
    for i in fwd_paths_gain:
        x_gain = 1
        for j in i:
            x_gain *= j
        total_gains.append(x_gain)
    return total_gains


def get_gains(graph, path):
    gains = []
    length = len(path) - 1
    mod = length + 1
    for i in range(length):
        edge = graph.get_edge_data(path[i], path[(i + 1) % mod])
        weights = []
        for j in range(len(edge)):
            weights.append(edge[j]['weight'])
        gains.append(weights)
    gains = gain_multiply(gains)
    return get_all_fwdpath_gains(gains)
