# Pulp doesnt support math.inf that's why I have used an arbitrary big number
def get_input(i):
    if i == 1:
        return [[100000, 1, 15, 6],
                   [2, 100000, 7, 3],
                   [9, 6, 100000, 12],
                   [10, 4, 8, 100000]]
    else:
        print(f"Invalide input: {i}")
        return None, None
    