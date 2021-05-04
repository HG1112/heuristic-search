import numpy as np
from node import Node
from collections import deque
import logging

log = logging.getLogger('Search')
class Search:


    def __init__(self, initial_position, initial_state, goal_state, heuristic):
        self.grid_size = initial_state.shape[0]
        self.root = Node(initial_position, self.grid_size, [])
        self.init = initial_state
        self.goal = goal_state
        log.debug('Initial position : %s', initial_position)
        log.debug('Initial state :\n%s', initial_state)
        log.debug('Goal state :\n%s', goal_state)

    def find(self):
        log.debug('Root : %s', self.root)
        queue = deque()
        queue.append(self.root)
        while len(queue) != 0:
            node = queue.popleft()
            if self.test(node.apply(self.init), self.goal):
                return node
            for n in node.next():
                log.debug('Add node : %s', n)
                queue.append(n)
        return None

    def test(self, a, b):
        return np.array_equal(a, b)
