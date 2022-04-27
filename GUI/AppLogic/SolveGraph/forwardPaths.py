import networkx as nx

def generate_all_fwdpaths(graph: nx.DiGraph, source, target):
    return nx.all_simple_paths(graph, source, target)

def get_total_gain(path_gains):
    k = 0
    path_gain = 1
    for gain in path_gains:
        path_gain *= float(gain)
        k += 1
     
    return path_gain

def get_fwdPath_gain(graph: nx.DiGraph, path):
    gains = []
    length = len(path) - 1
    mod = length + 1
    for i in range(length):
        edgeData = graph.get_edge_data(path[i], path[(i + 1) % mod])
        gains.append(edgeData['weight'])
    return get_total_gain(gains)
