import numpy as np

def a_star(node, initial_state, current_state):
    return 2*(abs(dx) + abs(dy))

def manhatten_distance(node, initial_state, current_state):
    n = goal_state.shape[0]
    dx, dy = node.position - (n,n)
    return abs(dx) + abs(dy)

def misplaced_tile(node, initial_state, current_state):
    return len(item for item in np.equal(node.apply(initial_state), goal_state) if item)

def no_cost(node, initial_state, current_state):
    return 0
