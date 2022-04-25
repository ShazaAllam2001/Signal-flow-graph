import itertools
import networkx as nx


def remove_duplicates(paths):
    res = []
    for i in paths:
        if i not in res:
            res.append(i)
    return res


def merge_gains(gains):
    return list(itertools.product(*gains))


def get_all_fwdpath_gains(fwd_paths_gain):
    total_gains = []
    for i in fwd_paths_gain:
        k = 0
        flag = True
        x_gain = ""
        for j in i:
            if isinstance(j, int):
                if j == 1:
                    j = ""
                    flag = False
                else:
                    j = str(j)
            x_gain += j
            k += 1
            if k <= len(i)-1 and flag:
                x_gain += '*'
            flag = True
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
    gains = merge_gains(gains)
    return get_all_fwdpath_gains(gains)
