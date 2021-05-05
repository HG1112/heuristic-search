import copy
import logging 

log = logging.getLogger('State')
class State:

    def __init__(self, size, state = None, blank_position = None, prev_states = None):
        if not state:
            self.state = [i+1 for i in range(size**2)]
            log.debug('default state')
        else:
            self.state = state

        if blank_position == None:
            self.blank_position = size**2 -1
            self.state[size**2 -1] = 0
            log.debug('default blank position')
        else:
            self.blank_position = blank_position

        self.N = size

        if not prev_states:
            self.previous_states = []
            log.debug('default previous states')
        else:
            self.previous_states = prev_states

        log.debug('Construct State of Tile Puzzle: %s | %s | %s | %s', size, state, blank_position, prev_states)
        log.debug('\tstate: %s', self.state)
        log.debug('\tblank: %s', self.blank_position)
        log.debug('\tN: %s', self.N)
        log.debug('\tprevs: %s', self.previous_states)

    def add_prev_state(self, prev):
        self.previous_states.append(prev)

    def add_prev_states(self, prevs):
        self.previous_states.extend(prevs)

    def get_prev_states(self):
        return self.previous_states

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state

    def get_blank_position(self):
        return self.blank_position

    def set_blank_position(self, new_position):
        self.blank_position = new_position


    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        flag = True
        other_state = other.get_state()
        for i in range(self.N**2):
            if flag:
                flag = (self.state[i] == other_state[i])
            else:
                return False
        return flag

    def __repr__(self):
        return '[' + ','.join([str(i) for i in self.state]) + '](' + str(self.blank_position) + ')'

    def to_string(self):
        return '\n'.join([' , '.join([str(self.state[i*self.N + j]) for j in range(self.N)]) for i in range(self.N)])

    def next(self):
        next_states = []

        x = int(self.blank_position / self.N)
        y = int(self.blank_position % self.N)
        log.debug('Current Positon of blank: %s', (x,y))

        for (i,j) in [(x+1, y), (x-1, y), (x, y+1), (x,y-1)]:

            log.debug('Consider neighbor at %s', (i,j))
            if 0 <= i < self.N and (0 <= j < self.N):

                state = copy.deepcopy(self.state)
                prev = copy.deepcopy(self.previous_states)
                prev.append(self)

                new_position = i*self.N + j
                state[self.blank_position] = state[new_position]
                state[new_position] = 0

                next_state = State(self.N, state, new_position, prev)
                if next_state not in self.previous_states:
                    log.debug('can move to %s', (i,j))
                    next_states.append(next_state)

        return next_states
