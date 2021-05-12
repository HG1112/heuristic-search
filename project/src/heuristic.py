from math import sqrt
import logging 

log = logging.getLogger('Heuristic')

def manhattan_distance(current_board):
    '''
    Returns the manhattan distance between given and goal boards.
    '''
    N = len(current_board)
    n = int(sqrt(N))
    sum = 0
    
    # loop over all the positions in the board
    for k in range(N):
        val = current_board[k]
        # position of the cell in given board
        i,j = int(k/n), k%n
        if val :
            # Position of the cell in goal board
            x , y = int((val-1)/n), (val-1)%n
        else:
            x , y = n-1, n-1
        # calculation of manhattan distance
        dist = (abs(x-i) + abs(y-j))
        log.debug('Manhattan distance between %s and %s : %s', (i,j), (x,y), dist)
        sum += dist
    return sum


def misplaced_tile(current_board):
    '''
    Returns the number of misplaced tiles in the current board with repect to the goal board.
    '''
    count = 0
    N = len(current_board)
    for i in range(N-1):
        # flag returns whether the tile or cell is misplaced or not
        flag = int(i+1 != current_board[i])
        log.debug('Misplaced tile ? - %s / %s : %s', i+1, current_board[i], flag)
        # count returns the number of misplaced tiles in the board
        count += flag
    log.debug('Misplaced tile ? - %s / %s', 0, current_board[N-1])
    count += int(0 != current_board[N-1])
    return count

def no_cost(current_board):
    '''
    Returns 0 as uniform cost search has no heuristic cost
    '''
    log.debug('No cost')
    return 0


def a_star(state, heuristic):
    '''
    Returns the a star cost of a given state with repect to the given heuristic function
    '''
    # depth of the given state with respect to the root of the search tree
    g = state.depth
    # cost of the given heuristic function for a given state
    h = heuristic(state.puzzle.board)
    log.debug('A-star : %s + %s', g, h)
    return g+h
