import logging
from random import random
from termcolor import colored

from project.src.search import Search
from project.src.state import State
from project.src.heuristic import *
from project.src.puzzle import create_puzzle, Puzzle

log_format='[%(name)s] : %(message)s'
logging.basicConfig(level=logging.INFO , format=log_format)

log = logging.getLogger('Solver')



WELCOME = colored('Welcome to NxN Sliding Tile Puzzle Solver', 'blue')
ASK_N = colored('Enter the side of the puzzle :', 'blue')
BLANK_TILE = colored('Beware, 0 is a must and acts as blank position', 'red')
ASK_ROW = colored('Enter the space-seperated values of row ', 'blue')

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
    search = Search(n)
    result = search.solve(state, manhattan_distance)
    log.info(colored('Path: \n %s', 'green'),colored(' -> '.join([ str(coord) for coord in result.path_from_root()]), 'cyan'))

if __name__ == '__main__':
    log.info(WELCOME)
    main()

