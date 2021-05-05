import numpy as np
from project.src.search import Search
from project.src.heuristic import *

goal = np.array([[1,2], [3,0]])
search = Search(goal)

def test_1():
    initial_state = np.array([[1,2], [0,3]])
    result = search.find(initial_state, no_cost)
    assert search.test(result.apply(initial_state), goal)

def test_2():
    initial_state = np.array([[0,2], [1,3]])
    result = search.find(initial_state, no_cost)
    assert search.test(result.apply(initial_state), goal)

def test_3():
    initial_state = np.array([[2,0], [1,3]])
    result = search.find(initial_state, no_cost)
    assert search.test(result.apply(initial_state), goal)

def test_4():
    initial_state = np.array([[2,3], [1,0]])
    result = search.find(initial_state, no_cost)
    assert search.test(result.apply(initial_state), goal)

def test_5():
    initial_state = np.array([[2,3], [0,1]])
    result = search.find(initial_state, no_cost)
    assert search.test(result.apply(initial_state), goal)
