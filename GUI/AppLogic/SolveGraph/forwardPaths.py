import networkx as nx

def generate_all_fwdpaths(graph: nx.DiGraph, source, target):
    return nx.all_simple_paths(graph, source, target)

def get_total_gain(path_gains):
    k = 0
    isString = True
    path_gain_number = 1
    path_gain_str = ""
    for gain in path_gains:
        gain = str(gain)
        if gain.isnumeric():
            isString = False
            path_gain_number *= float(gain)
        else:
            path_gain_str += gain
        k += 1
        if k <= len(path_gains)-1 and isString:
            path_gain_str += '*'
        isString = True

    if path_gain_str == "":
        return path_gain_number
    else:
        return path_gain_str

def get_fwdPaths_gains(graph: nx.DiGraph, path):
    gains = []
    length = len(path) - 1
    mod = length + 1
    for i in range(length):
        edgeData = graph.get_edge_data(path[i], path[(i + 1) % mod])
        gains.append(edgeData['weight'])
    return get_total_gain(gains)
