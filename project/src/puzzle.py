import logging 
from copy import deepcopy
from project.src.move import Moves

log = logging.getLogger('Puzzle')
class Puzzle:

    def __init__(self, board, blank_pos, shape):
        self.board = board
        self.blank_pos = blank_pos
        self.shape = shape
    
    def __repr__(self):
        return '[' + ','.join([str(e) for e in self.board]) + ']{}'.format(self.blank_pos)

    def __eq__(self, other):
        if other.blank_pos != self.blank_pos:
            return False
        l,b = self.shape
        for i in range(l*b):
            if self.board[i] != other.board[i]:
                return False
        return True

    def apply_move(self, move):
        log.debug('Apply move %s on given puzzle', move)

        copy = deepcopy(self.board)
        log.debug('Deepcopy of current board')

        l , b = self.shape
        log.debug('Shape of puzzle : %s', (l,b))

        x , y = self.blank_pos
        log.debug('Blank of puzzle : %s', (x,y))

        curr = x*l + y
        if move == Moves.UP:
            x+=1
        if move == Moves.DOWN:
            x-=1
        if move == Moves.LEFT:
            y-=1
        if move == Moves.RIGHT:
            y+=1
        next = x*l + y
        log.debug('Next Blank of puzzle : %s', (x,y))

        copy[curr], copy[next] = copy[next], copy[curr]

        return Puzzle(copy, (x,y), (l,b))
    
    def possible_moves(self, not_allowed):
        log.debug('Possible moves for given puzzle and not_allowed %s', not_allowed)

        l , b = self.shape
        log.debug('Shape of puzzle : %s', (l,b))

        x , y = self.blank_pos
        log.debug('Blank of puzzle : %s', (x,y))

        log.debug('Initializing possible moves')
        moves = []

        if 0 <= x-1 <= l-1 and (x-1,y) != not_allowed:
            log.debug('down : possible')
            moves.append((Moves.DOWN, self.apply_move(Moves.DOWN)))

        if 0 <= x+1 <= l-1 and (x+1,y) != not_allowed:
            log.debug('up : possible')
            moves.append((Moves.UP, self.apply_move(Moves.UP)))

        if 0 <= y-1 <= b-1 and (x,y-1) != not_allowed:
            log.debug('left : possible')
            moves.append((Moves.LEFT, self.apply_move(Moves.LEFT)))

        if 0 <= y+1 <= b-1 and (x,y+1) != not_allowed:
            log.debug('right : possible')
            moves.append((Moves.RIGHT, self.apply_move(Moves.RIGHT)))

        return moves
    
    def randomize(self, depth):
        pass

def create_puzzle(n):
    log.debug('Create puzzle of side %s', n)
    board = [ i+1 for i in range(n**2) ]
    board[n**2 - 1] = 0
    return Puzzle(board, (n-1,n-1), (n,n))

