from math import sqrt
import logging 

log = logging.getLogger('Heuristic')

def manhattan_distance(current_board):
    N = len(current_board)
    n = int(sqrt(N))
    sum = 0
    for k in range(N):
        val = current_board[k]
        i,j = int(k/n), k%n
        if val :
            x , y = int((val-1)/n), (val-1)%n
        else:
            x , y = n-1, n-1
        log.debug('Manhattan distance between %s and %s', (i,j), (x,y))
        sum += (abs(x-i) + abs(y-j))
    return sum


def misplaced_tile(current_board):
    count = 0
    N = len(current_board)
    for i in range(N-1):
        log.debug('Misplaced tile ? - %s / %s', i+1, current_board[i])
        count += int(i+1 != current_board[i])
    log.debug('Misplaced tile ? - %s / %s', 0, current_board[N-1])
    count += int(0 != current_board[N-1])
    return count

def no_cost(current_board):
    log.debug('No cost')
    return 0


def a_star(state, heuristic):
    g = state.depth
    h = heuristic(state.puzzle.board)
    log.debug('A-star : %s + %s', g, h)
    return g+h
