import logging
from heapq import heappush, heapify, heappop
from project.src.state import State
from project.src.puzzle import create_puzzle
from project.src.heuristic import *

log = logging.getLogger('Search')
class Search:

    def __init__(self, n):
        log.info('Search for complete puzzle of size %s', n*n -1)
        self.goal = create_puzzle(n)
        log.info('Goal : %s', self.goal)

    def solve(self, initial_state, heuristic):
        visited = []

        log.info('Initializing priority queue')
        queue = [(a_star(initial_state, heuristic), initial_state)]
        heapify(queue)

        log.info('Loop through the queue')
        while queue:
            priority, state = heappop(queue)
            log.debug('Priority : %s , State : %s', priority, state)

            if state.puzzle in visited:
                log.debug('Skip : %s', state)
                continue

            log.debug('Check : %s', state)
            if state.puzzle == self.goal:
                return state

            log.debug('adding its children to priority queue')
            for st in state.next_possible_states(visited):
                pr = a_star(state, heuristic)
                log.debug('Child: Priority : %s, State : %s', pr, st)
                heappush(queue, (pr, st))

        return None
