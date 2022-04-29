from pulp import LpProblem, LpMinimize, LpVariable, LpInteger
from input import get_input
from utils import powerset

def form_LIP(): 
    c = get_input(1)  # path_cost
    nodes_num = len(c[0])
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
            objective += x[i][j] * c[i][j]
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
        c = None
        for i in subset:
            for j in subset:
                c += x[i][j]
        problem += c <= (len(subset) - 1)

    problem.solve()
    print(f"Objective is: {problem.objective}")
    for i in range(0, nodes_num):
        for j in range(0, nodes_num):
            if x[i][j].varValue == 1:
                print(f"{i} -> {j}")

form_LIP()