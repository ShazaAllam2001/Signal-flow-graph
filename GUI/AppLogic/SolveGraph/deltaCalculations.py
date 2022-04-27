import networkx as nx

from AppLogic.SolveGraph.loops import get_loop_gain

def get_non_touching_loops_with_a_path(path, loops):
    non_touching_loops = []
    for loop in loops:
        intersection = [node for node in path if node in loop]
        if not intersection:
            non_touching_loops.append(loop)
    return non_touching_loops


def calculate_delta_i(graph: nx.DiGraph, path, loops, non_touching_loops):
    delta_i = 1
    loops_not_touching_path = get_non_touching_loops_with_a_path(path, loops)

    if loops_not_touching_path:
        total = 0
        for loop in loops_not_touching_path:
            total += get_loop_gain(graph, loop)
        delta_i -= total
    else:
        return delta_i

    sign = 1
    for non_touching_group in non_touching_loops:
        total = 0
        for loops in non_touching_group:
            prod = 1
            for loop in loops:
                if loop in loops_not_touching_path:
                    prod *= get_loop_gain(graph, loop)
                else:
                    prod = 0
                    break
            total += prod
        delta_i += sign * total
        sign *= -1
    return delta_i


def calculate_delta(graph: nx.DiGraph, loops, non_touching_loops):
    delta = 1
    total = 0
    for loop in loops:
        total += get_loop_gain(graph, loop)
    delta -= total

    sign = 1
    for non_touching_group in non_touching_loops:
        total = 0
        for loops in non_touching_group:
            prod = 1
            for loop in loops:
                prod *= get_loop_gain(graph, loop)
            total += prod
        delta += sign * total
        sign *= -1
    return delta
