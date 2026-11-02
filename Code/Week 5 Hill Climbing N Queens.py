def cost(state):
    n = len(state)
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def get_neighbors(state):
    neighbors = []
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            neighbor = state.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)

    return neighbors


def hill_climbing(initial_state):
    current = initial_state

    while True:
        current_cost = cost(current)

        if current_cost == 0:
            return current

        best_neighbor = current
        best_cost = current_cost

        for neighbor in get_neighbors(current):
            neighbor_cost = cost(neighbor)

            if neighbor_cost < best_cost:
                best_neighbor = neighbor
                best_cost = neighbor_cost

        if best_cost >= current_cost:
            return current

        current = best_neighbor


initial_state = [3, 1, 2, 0]

solution = hill_climbing(initial_state)

print("Solution:", solution)
print("Cost:", cost(solution))