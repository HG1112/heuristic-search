import logging
from heapq import heappush, heapify, heappop
from project.src.state import State
from project.src.puzzle import create_puzzle
from project.src.heuristic import *

log = logging.getLogger('Search')
class Search:

    def __init__(self, n):
        log.debug('Search for complete puzzle of size %s', n*n)
        self.goal = create_puzzle(n)
        log.info('Goal : %s', self.goal)

    def solve(self, initial_state, heuristic):
        visited = []

        log.debug('Initializing priority queue')
        queue = [(a_star(initial_state, heuristic), initial_state)]
        heapify(queue)
        
        max_queue_length = len(queue)
        states_expanded = 0

        log.debug('Loop through the queue')
        while queue:
            priority, state = heappop(queue)            
            log.info('Expanding with priority %s and depth %s',  priority, state.depth)
            log.info('Matrix \n%s ', state.puzzle.matrix_repr() )
            states_expanded+=1

            if state.puzzle in visited:
                log.debug('Skip : %s', state)
                continue

            log.debug('Check : %s', state)
            if state.puzzle == self.goal:
                return max_queue_length, states_expanded, state

            log.debug('adding its children to priority queue')
            for st in state.next_possible_states(visited):
                pr = a_star(state, heuristic)
                log.debug('Child: Priority : %s, State : %s', pr, st)
                heappush(queue, (pr, st))

            max_queue_length = max(max_queue_length, len(queue))

        return max_queue_length, states_expanded, None
