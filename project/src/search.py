from collections import deque
import numpy as np
import logging
from project.src.node import Node

log = logging.getLogger('Search')
class Search:

    def __init__(self, goal_state):
        self.grid_size = goal_state.shape[0]
        initial_position = (self.grid_size-1, self.grid_size-1)
        self.root = Node(initial_position, self.grid_size, [])
        self.goal = goal_state
        log.debug('Goal state :\n%s', goal_state)

    def find(self, initial_state, heuristic):
        queue = deque()
        queue.append(self.root)
        while len(queue) != 0:
            node = queue.popleft()
            if self.test(node.apply(initial_state), self.goal):
                return node
            for n in sorted(node.next(), key = lambda node : heuristic(node, initial_state, self.goal) , reverse = True):
                log.debug('Add node : %s', n)
                queue.append(n)
        return None

    def test(self, a, b):
        return np.array_equal(a, b)
