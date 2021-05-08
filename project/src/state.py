class State:

    def __init__(self, puzzle, parent):
        self.puzzle = puzzle
        self.parent = parent
        self.cost = 1
        if parent:
            self.cost += parent.cost

    def next_possible_states(self, visited):
        if self.parent:
            return [ State(puz, self) for move , puz in self.puzzle.possible_moves(self.parent.puzzle.blank_pos) if puz not in visited]
        else:
            return [ State(puz, self) for move , puz in self.puzzle.possible_moves(None) if puz not in visited]


    def __repr__(self):
        return 'State(' + ' | '.join(['Parent : {}'.format(self.parent) , 'Puzzle : {}'.format(self.puzzle), 'Cost : {}'.format(self.cost) ]) + ")"
