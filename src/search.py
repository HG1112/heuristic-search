from collections import deque
import numpy as np
import logging
from node import Node

log = logging.getLogger('Search')
class Search:

    def __init__(self, initial_state):
        self.grid_size = initial_state.shape[0]
        initial_position = (self.grid_size-1, self.grid_size-1)
        self.root = Node(initial_position, self.grid_size, [])
        self.init = initial_state
        log.debug('Initial state :\n%s', initial_state)

    def find(self, goal_state, heuristic):
        queue = deque()
        queue.append(self.root)
        while len(queue) != 0:
            node = queue.popleft()
            if self.test(node.apply(self.init), goal_state):
                return node
            for n in sorted(node.next(), key = lambda node : heuristic(node, self.init, goal_state) , reverse = True):
                log.debug('Add node : %s', n)
                queue.append(n)
        return None

    def test(self, a, b):
        return np.array_equal(a, b)
