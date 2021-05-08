from project.src.heuristic import *
from project.src.state import State
from project.src.puzzle import create_puzzle

def test_manhattan_distance():
    puzzle = create_puzzle(3)
    state = State(puzzle, None)
    assert manhattan_distance(state.puzzle.board) == 0
    puzzle.board = [0,2,3, 1,5,6, 4,7,8]
    state = State(puzzle, None)
    assert manhattan_distance(state.puzzle.board) == 8

def test_misplaced_tile():
    puzzle = create_puzzle(3)
    state = State(puzzle, None)
    assert misplaced_tile(state.puzzle.board) == 0
    puzzle.board = [0,2,3, 1,5,6, 4,7,8]
    state = State(puzzle, None)
    assert misplaced_tile(state.puzzle.board) == 5

def test_no_cost():
    puzzle = create_puzzle(3)
    state = State(puzzle, None)
    assert no_cost(state.puzzle.board) == 0
    puzzle.board = [0,2,3, 1,5,6, 4,7,8]
    state = State(puzzle, None)
    assert no_cost(state.puzzle.board) == 0

def test_a_star():
    puzzle = create_puzzle(3)
    state = State(puzzle, None)
    assert a_star(state, no_cost) == 1
    assert a_star(state, manhattan_distance) == 1
    assert a_star(state, misplaced_tile) == 1
    puzzle.board = [0,2,3, 1,5,6, 4,7,8]
    state = State(puzzle, None)
    state.cost = 4
    assert a_star(state, no_cost) == 4
    assert a_star(state, manhattan_distance) == 12
    assert a_star(state, misplaced_tile) == 9
