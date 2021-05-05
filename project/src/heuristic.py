import numpy as np

def a_star(node, initial_state, goal_state):
    g = manhattan_distance(node, initial_state, goal_state)
    f = manhattan_distance(node, initial_state, goal_state)
    return g+f

def manhattan_distance(node, initial_state, goal_state):
    x, y = np.where(goal_state == 0)
    dx = node.position[0] - x 
    dy = node.position[1] - y 
    return abs(dx) + abs(dy)

def misplaced_tile(node, initial_state, goal_state):
    return len([ cell for row in np.equal(node.apply(initial_state), goal_state) for cell in row if not cell ])

def no_cost(node, initial_state, goal_state):
    return 0
