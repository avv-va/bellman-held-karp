import math

from input import get_input
from utils import powerset, print_path


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


def get_tsp_path(path_cost):
    nodes_num = len(path_cost[0])
    origin = 0 # It doesn't really matter where you choose as origin since you are doing a full tour
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
