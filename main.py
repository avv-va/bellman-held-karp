from input import get_input
import math
from itertools import chain, combinations


def calculate_cost(origin, dest, via, cost_matrix, path_cost, parent_matrix):
    if len(via) == 0:
        return cost_matrix[via][dest], parent_matrix[via][dest]
    elif len(via) == 1:
        return path_cost[origin][via[0]] + path_cost[via[0]][dest], via[0]
    else:
        parent = -1
        min_cost = math.inf
        for p in via:
            other_vias = tuple([v for v in via if v != p])
            c = path_cost[p][dest] + cost_matrix[other_vias][p]
            if c <= min_cost:
                min_cost = c
                parent = p
        return min_cost, parent


def powerset(s):
    return list(
        chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


def calculate_path(parent_matrix, origin, final_via):
    dest = origin
    via = final_via
    path = [dest]
    while via != ():
        new_dest = parent_matrix[via][dest]
        new_via = tuple([i for i in via if i != new_dest])
        dest, via = new_dest, new_via
        path.append(dest)
    path.append(origin)

    return path


def get_tsp_path(origin, path_cost):
    nodes_num = len(path_cost[0])
    possible_paths = powerset([i for i in range(0, nodes_num) if i != origin])

    cost_matrix = {}
    parent_matrix = {}
    for via in possible_paths:
        cost_matrix[via] = [-1 for _ in range(0, nodes_num)]
        parent_matrix[via] = [-1 for _ in range(0, nodes_num)]

    for dest in range(0, nodes_num):
        cost_matrix[()][dest] = path_cost[origin][dest]
        parent_matrix[()][dest] = origin

    for via in possible_paths:
        for dest in range(0, nodes_num):
            cost_matrix[via][dest], parent_matrix[via][dest] = calculate_cost(
                origin, dest, via, cost_matrix, path_cost, parent_matrix)
    

    final_via = tuple([i for i in range(0, nodes_num) if i != origin])
    optimal_cost = cost_matrix[final_via][origin]

    path = calculate_path(parent_matrix, origin, final_via)
    
    return optimal_cost, path


def print_path(path):
    for i in range(len(path)-1, -1, -1):
        if i == 0:
            print(path[i], end="\n")
        else:
            print(path[i], end=" -> ")
        


def print_matrix(cost, parent):
    for vias in cost:
        for dest in range(0, len(cost[vias])):
            print(
                f'dest={dest}, via={vias}, cost={cost[vias][dest]}, parent={parent[vias][dest]}'
            )


if __name__ == '__main__':
    origin, path_cost = get_input(1)
    optimal_cost, path = get_tsp_path(origin, path_cost)
    print("Optimal cost is: ", optimal_cost)
    print_path(path)
