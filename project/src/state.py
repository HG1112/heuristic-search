class State:
    '''
    Representation of a node in the search tree. \n
    It has a puzzle instance, a pointer to it's parent and it's depth in the search tree
    '''
    def __init__(self, puzzle, parent):
        self.puzzle = puzzle
        self.parent = parent
        self.depth = 1
        if parent:
            self.depth += parent.depth

    def next_possible_states(self, visited):
        '''
        Returns all possible nodes for a given state which haven't been already visited in the search tree.
        '''
        if self.parent:
            return [ State(puz, self) for move , puz in self.puzzle.possible_moves(self.parent.puzzle.blank_pos) if puz not in visited]
        else:
            return [ State(puz, self) for move , puz in self.puzzle.possible_moves(None) if puz not in visited]


    def __repr__(self):
        return 'State(' + ' | '.join(['Parent : {}'.format(self.parent) , 'Puzzle : {}'.format(self.puzzle), 'Depth : {}'.format(self.depth) ]) + ")"


    def __lt__(self, other):
        return self.depth < other.depth

    def __le__(self, other):
        return self.depth <= other.depth

    def path_from_root(self):
        '''
        Returns the path of blank to goal position
        '''
        path = []
        parent = self
        while parent:
            path.insert(0,parent.puzzle.blank_pos)
            parent = parent.parent
        return path
