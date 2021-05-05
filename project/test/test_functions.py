from project.src.functions import swap_cell , get_neighbors
import pytest

def test_get_neighbors():
    grid_size = 3
    assert set(get_neighbors((1,1), 3)) == set([(2,1), (1,2), (1,0), (0,1)])
    assert set(get_neighbors((0,1), 3)) == set([(1,1), (0,0), (0,2)])
    assert set(get_neighbors((0,0), 3)) == set([(0,1), (1,0)])


def test_swap_cell():
    pos1 = (0,0)
    pos2 = (0,1)
    state = [[1,2],[3,0]]
    swap_cell(pos1, pos2, state) 
    assert state == [[2,1], [3,0]]
    pos2 = (1,1)
    with pytest.raises(ValueError):
        swap_cell(pos1, pos2, state)
