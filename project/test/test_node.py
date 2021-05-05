import numpy as np
from project.src.node import Node

def test_apply():
    goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    initial_state = np.array([[1,2,3], [4,0,6], [7,5,8]])
    node = Node((1,1), 3, [(2,2), (2,1)])
    actual = node.apply(initial_state)
    assert np.array_equal(actual , goal_state )


def test_next():
    node = Node((2,2), 3, [])
    assert node.next() == [Node((1,2), 3, [(2,2)]), Node((2,1), 3, [(2,2)])]


    
