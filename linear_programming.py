from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, value
from utils import powerset

def solve_by_LIP(path_cost): 
    nodes_num = len(path_cost[0])
    problem = LpProblem('TravellingSalesmanProblem', LpMinimize)
    
    x = [] # vars
    for i in range(0, nodes_num):
        x_ = []
        for j in range(0, nodes_num):
            x_.append(LpVariable(f'x{i}{j}', lowBound=0, upBound=1, cat=LpInteger))
        x.append(x_)

    objective = 0
    for i in range(0, nodes_num):
        for j in range(0, nodes_num):
            objective += x[i][j] * path_cost[i][j]
    problem += objective, 'objective function'
    
    # each node has only one outgoing edge and one ingoing edge
    for i in range(0, nodes_num):
        c1, c2 = None, None
        for j in range(0, nodes_num):
            c1 += x[i][j]
            c2 += x[j][i]
        problem += c1 == 1
        problem += c2 == 1
    
    # eliminate subsets tours
    power_set = powerset([i for i in range(0, nodes_num)])
    power_set.remove(())
    for subset in power_set:
        if len(subset) == nodes_num:
            continue
        path_cost = None
        for i in subset:
            for j in subset:
                path_cost += x[i][j]
        problem += path_cost <= (len(subset) - 1)

    problem.solve()

    path = ''  # TODO: Better return a path type similar to BHK
    for i in range(0, nodes_num):
        for j in range(0, nodes_num):
            if x[i][j].varValue == 1:
                path += f'{i} -> {j}, '
    
    return value(problem.objective), path
