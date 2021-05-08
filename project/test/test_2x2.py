from project.src.state import State
from project.src.puzzle import Puzzle , create_puzzle

def test_2x2():
    puz = create_puzzle(2)
    state = State(puz, None)
    visited = []
    bfs = [state]
    while bfs:
        s = bfs.pop(0)
        if s.puzzle in visited:
            continue
        for st in s.next_possible_states(visited):
            bfs.append(st)
        visited.append(s.puzzle)
    assert len(visited) == 12

