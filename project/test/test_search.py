import numpy as np
from project.src.node import Node
from project.src.search import Search
from project.src.heuristic import *

def test_test():
    initial_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    search = Search(goal_state)
    assert search.test(initial_state, goal_state)
    initial_state = np.array([[0,2,3], [1,5,6], [4,7,8]])
    assert not search.test(initial_state, goal_state)

def test_find_nocost():
    initial_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    search = Search(goal_state)
    result = search.find(initial_state, no_cost)
    assert result == Node((2,2), 3, [])
    assert search.test(result.apply(initial_state), goal_state)
    initial_state = np.array([[1,2,3], [0,5,6], [4,7,8]])
    result = search.find(initial_state, no_cost)
    assert result == Node((1,0), 3, [(2,2), (2,1), (2,0)])
    assert search.test(result.apply(initial_state), goal_state)
    initial_state = np.array([[1,2,3], [4,5,6], [8,7,0]])
    result = search.find(initial_state, no_cost)
    assert result == None

def test_find_misplaced_tile():
    initial_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    search = Search(goal_state)
    result = search.find(initial_state, misplaced_tile)
    assert result == Node((2,2), 3, [])
    assert search.test(result.apply(initial_state), goal_state)
    initial_state = np.array([[1,2,3], [0,5,6], [4,7,8]])
    result = search.find(initial_state, misplaced_tile)
    assert result == Node((1,0), 3, [(2,2), (2,1), (2,0)])
    assert search.test(result.apply(initial_state), goal_state)
    initial_state = np.array([[1,2,3], [4,5,6], [8,7,0]])
    result = search.find(initial_state, misplaced_tile)
    assert result == None

def test_find_manhattan_distance():
    initial_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    search = Search(goal_state)
    result = search.find(initial_state, manhattan_distance)
    assert result == Node((2,2), 3, [])
    assert search.test(result.apply(initial_state), goal_state)
    initial_state = np.array([[1,2,3], [0,5,6], [4,7,8]])
    result = search.find(initial_state, manhattan_distance)
    assert result == Node((1,0), 3, [(2,2), (2,1), (2,0)])
    assert search.test(result.apply(initial_state), goal_state)
    initial_state = np.array([[1,2,3], [4,5,6], [8,7,0]])
    result = search.find(initial_state, manhattan_distance)
    assert result == None

def test_find_astar():
    initial_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    search = Search(goal_state)
    result = search.find(initial_state, a_star)
    assert result == Node((2,2), 3, [])
    assert search.test(result.apply(initial_state), goal_state)
    initial_state = np.array([[1,2,3], [0,5,6], [4,7,8]])
    result = search.find(initial_state, a_star)
    assert result == Node((1,0), 3, [(2,2), (2,1), (2,0)])
    assert search.test(result.apply(initial_state), goal_state)
    initial_state = np.array([[1,2,3], [4,5,6], [8,7,0]])
    result = search.find(initial_state, a_star)
    assert result == None
