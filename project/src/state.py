class State:

    def __init__(self, size):
        self.state = [i for i in range(size**2 - 1)]
        self.blank_position = size**2 -1
        self.state[size**2 -1] = 0
        self.N = size
        self.previous_states = []

    def __init__(self, size, state, blank_position, prev_states):
        self.state = state
        self.blank_position = blank_position
        self.N = size
        self.previous_states = prev_states

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
                    flag = (self.state[i][j] == other_state[i][j])
                else:
                    return False
        return flag

    def __repr__(self):
        return '\n'.join([' , '.join([self.state[i][j] for j in range(N)]) for i in range(N)])

    def next(self):
        next_states = []
        x = self.blank_position / self.N
        y = self.blank_position % self.N
        for (i,j) in [(x+1, y), (x-1, y), (x, y+1), (x,y-1)] if 0 <= i < self.N and (0 <= j < self.N)]:
            state = self.state.deepcopy()
            state[i][j], state[x][y] = state[x][y] , state[i][j]
            next_state = State(self.N, state, x*self.N + y, [])
            if next_state not in self.previous_states:
                next_state.add_prev_states(self.previous_states)
                next_states.append(next_state)
        return next_states
