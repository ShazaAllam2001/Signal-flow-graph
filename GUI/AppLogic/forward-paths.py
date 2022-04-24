def turn_to_list(gains):
    return list(itertools.product(*gains))
    

def multiply_gains(fwd_paths_gain):
    total_gains= []
    for i in fwd_paths_gain:
        x_gain=1
        for j in i:
            x_gain*=j
        total_gains.append(x_gain)
    return total_gains


def get_gains(graph,path):
    gains = []
    length = len(path) - 1
    mod = length +  1 
    for i in range(length):
         edge = graph.get_edge_data(path[i], path[(i + 1) % mod])
         weights = []
         for j in range(len(edge)):
             weights.append(edge[j]['weight'])
         gains.append(weights)
    gains = turn_to_list(gains)
    return multiply_gains(gains)
