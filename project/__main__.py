import logging
import time
from random import random
from termcolor import colored

from project.src.search import Search
from project.src.state import State
from project.src.heuristic import *
from project.src.puzzle import create_puzzle, Puzzle

## Basic logging configuration
log_format='%(message)s'
logging.basicConfig(level=logging.INFO , format=log_format)

log = logging.getLogger('Solver')

## console messages
WELCOME = colored('Welcome to NxN Sliding Tile Puzzle Solver', 'blue')
BLANK_TILE = colored('Beware, 0 is a must and acts as blank position', 'red')
ASK_N = colored('Enter the side of the puzzle :', 'blue')
ASK_ROW = colored('Enter the space-seperated values of row ', 'blue')
ASK_H = colored('Choose heuristic for optimal search -\n' + \
        '(1) Uniform Cost Search\n' + \
        '(2) A* with Misplaced Tile Heuristic\n' + \
        '(3) A* with Manhattan distannce heuritstic\n' + \
        'DEFAULT - Uniform cost search :', 'blue')

## initilaize a n x n puzzle
def get_puzzle(n):
    '''
    Returns a puzzle of shape n x n and blank at (n-1, n-1)
    '''
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
    '''
    Main function of project
    '''

    # Ask for side of the puzzle
    n = int(input(ASK_N))
    N = n**2
    log.info(BLANK_TILE)

    # Get a puzzle of shape n x n
    puzzle = get_puzzle(n)

    # initilaize the state of the given puzzle
    state = State(puzzle, None)

    # defualt heuristic is uniform cost search
    heuristic = no_cost

    # ask for heuristic function
    h = int(input(ASK_H))
    if h == 1:
        heuristic = no_cost
    if h == 2:
        heuristic = misplaced_tile
    if h == 3:
        heuristic = manhattan_distance

    # Initilaize search for puzzle n x n
    search = Search(n)

    #solve for given state
    max_queue_length, states_expanded, result = search.solve(state, heuristic)
    log.info(colored('Path: %s', 'green'),colored(' -> '.join([ str(coord) for coord in result.path_from_root()]), 'cyan'))
    log.info(colored('Number of states expanded : {}'.format(states_expanded), 'green'))
    log.info(colored('Maximum length of priority queue : {}'.format(max_queue_length), 'green'))
    
    # stop time
    log.info(colored('Time taken for execution : {}'.format( (time.time() - start_time) ), 'green'))
    
if __name__ == '__main__':
    log.info(WELCOME)
    # start time
    start_time = time.time()
    main()