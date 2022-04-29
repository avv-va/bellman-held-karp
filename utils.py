from itertools import chain, combinations


def powerset(s):
    return list(
        chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


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
