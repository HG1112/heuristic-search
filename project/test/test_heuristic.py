from project.src.heuristic import *
from project.src.node import Node

def test_astar():
    initial_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    node = Node((2,2), 3, [])
    assert a_star(node, initial_state, goal_state) == 0
    initial_state = np.array([[0,2,3], [1,5,6], [4,7,8]])
    node = Node((0,0), 3, [])
    assert a_star(node, initial_state, goal_state) == 8

def test_manhattan_distance():
    initial_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    node = Node((2,2), 3, [])
    assert manhattan_distance(node, initial_state, goal_state) == 0
    initial_state = np.array([[0,2,3], [1,5,6], [4,7,8]])
    node = Node((0,0), 3, [])
    assert manhattan_distance(node, initial_state, goal_state) == 4

def test_misplaced_tile():
    initial_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    node = Node((2,2), 3, [])
    assert misplaced_tile(node, initial_state, goal_state) == 0
    initial_state = np.array([[0,2,3], [1,5,6], [4,7,8]])
    node = Node((0,0), 3, [])
    assert misplaced_tile(node, initial_state, goal_state) == 5

def test_no_cost():
    initial_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    node = Node((2,2), 3, [])
    assert no_cost(node, initial_state, goal_state) == 0
