import timeit
from input import get_input
from linear_programming import solve_by_LIP
from bellman_held_karp import get_tsp_path
from utils import print_path

if __name__ == '__main__':
    test_case = 1
    path_cost = get_input(test_case)

    start_LIP = timeit.default_timer()
    optimal_cost_LIP, path_LIP = solve_by_LIP(path_cost)
    stop_LIP = timeit.default_timer()

    start_BHK = timeit.default_timer()
    optimal_cost_BHK, path_BHK = get_tsp_path(path_cost)
    stop_BHK = timeit.default_timer()

    if optimal_cost_LIP == optimal_cost_BHK:
        print(f"Optimal cost is: {optimal_cost_LIP}")
        print_path(path_BHK)

        print(f"Execution time for Linear Integer Programming optimization: {str(stop_LIP - start_LIP)}")
        print(f"Execution time for Bellman Held Karp: {str(stop_BHK-start_BHK)}")
