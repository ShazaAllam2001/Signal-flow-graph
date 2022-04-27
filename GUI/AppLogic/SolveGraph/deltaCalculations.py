from loops import get_loops_gains
import networkx as nx


def get_non_touching_loops_with_a_path(path, loops):
    non_touching_loops = []
    for loop in loops:
        intersection = [node for node in path if node in loop]
        if not intersection:
            non_touching_loops += loop
    return non_touching_loops


def calculate_delta_i(graph: nx.DiGraph, path, loops, non_touching_loops):
    delta_i = 1
    loops_not_touching_path = get_non_touching_loops_with_a_path(path, loops)

    if loops_not_touching_path:
        total = 0
        for loop in loops_not_touching_path:
            total += get_loops_gains(graph, loop)
        delta_i -= total
    else:
        return delta_i

    sign = 1
    total = 0
    r = 2
    for non_touching_group in non_touching_loops:
        if len(non_touching_group) > r:
            r += 1
            delta_i += sign * total
            sign *= -1
            total = 0

        prod = 1
        for loop in non_touching_group:
            if loop in loops_not_touching_path:
                prod *= get_loops_gains(graph, loop)
            else:
                prod = 0
                break
        total += prod

    return delta_i


def calculate_delta(graph: nx.DiGraph, loops, non_touching_loops):
    delta = 1
    total = 0
    for loop in loops:
        total += get_loops_gains(graph, loop)
    delta -= total

    r = 2
    sign = 1
    total = 0
    for non_touching_group in non_touching_loops:
        if len(non_touching_group) > r:
            r += 1
            delta += sign * total
            total = 0
            sign *= -1
        prod = 1
        for loop in non_touching_group:
            prod *= get_loops_gains(graph, loop)
        total += prod
    return delta
