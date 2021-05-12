import logging 
from copy import deepcopy
from project.src.move import Moves

log = logging.getLogger('Puzzle')
class Puzzle:
    '''
    Abstraction to store a n x n square sliding tile puzzle
    '''
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
        '''
        Returns a new puzzle - blank position of given puzzle moves in the direction of given move. 
        '''
        log.debug('Apply move %s on given puzzle', move)

        # copy a given board
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

        # swap the current with given blank position
        copy[curr], copy[next] = copy[next], copy[curr]

        return Puzzle(copy, (x,y), (l,b))
    
    def possible_moves(self, not_allowed):
        '''
        Returns a list of tuples with next possible legal moves and the resultant puzzle after applying the move.\n
        not_allowed has the last legal position.  
        '''
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
    
    def matrix_repr(self):
        '''
        Represnts the board in a 2D array
        '''
        l,b = self.shape
        return '\n'.join( [' , '.join([ str(self.board[ i*l + j ]) for j in range(0,b)]) for i in range(0,l) ] )


def create_puzzle(n):
    '''
    Create the goal board for a side n
    '''
    log.debug('Create puzzle of side %s', n)
    board = [ i+1 for i in range(n**2) ]
    board[n**2 - 1] = 0
    return Puzzle(board, (n-1,n-1), (n,n))

