import logging
from random import random
from termcolor import colored

from project.src.search import Search
from project.src.state import State
from project.src.heuristic import *
from project.src.puzzle import create_puzzle, Puzzle

#log_format='[%(name)s] : %(message)s'
log_format='%(message)s'
logging.basicConfig(level=logging.INFO , format=log_format)

log = logging.getLogger('Solver')

WELCOME = colored('Welcome to NxN Sliding Tile Puzzle Solver', 'blue')
BLANK_TILE = colored('Beware, 0 is a must and acts as blank position', 'red')
ASK_N = colored('Enter the side of the puzzle :', 'blue')
ASK_ROW = colored('Enter the space-seperated values of row ', 'blue')
ASK_H = colored('Choose heuristic for optimal search -\n' + \
        '(1) Uniform Cost Search\n' + \
        '(2) A* with Misplaced Tile Heuristic\n' + \
        '(3) A* with Manhattan distannce heuritstic\n' + \
        'DEFAULT - Uniform cost search :', 'blue')

def get_puzzle(n):
    board = []
    blank_pos = None
    for i in range(0, n):
        row = input(ASK_ROW + str(i+1) + ' :').split(' ')
        for j in range(0, n):
            element = int(row[j])
            board.append(element)
            if not element:
                blank_pos = (i,j)
    return Puzzle(board, blank_pos, (n,n))

def main():
    n = int(input(ASK_N))
    N = n**2
    log.info(BLANK_TILE)

    puzzle = get_puzzle(n)
    state = State(puzzle, None)

    heuristic = no_cost
    h = int(input(ASK_H))
    if h == 1:
        heuristic = no_cost
    if h == 2:
        heuristic = misplaced_tile
    if h == 3:
        heuristic = manhattan_distance

    search = Search(n)
    max_queue_length, states_expanded, result = search.solve(state, heuristic)
    log.info(colored('Path: %s', 'green'),colored(' -> '.join([ str(coord) for coord in result.path_from_root()]), 'cyan'))
    log.info(colored('Number of states expanded : {}'.format(states_expanded), 'green'))
    log.info(colored('Maximum length of priority queue : {}'.format(max_queue_length), 'green'))

if __name__ == '__main__':
    log.info(WELCOME)
    main()

