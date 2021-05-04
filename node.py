from functions import get_neighbors, swap_cell
import logging 

log  = logging.getLogger('Node')
class Node:

    def __init__(self, pos, grid_size, visited):
        self.grid_size = grid_size
        self.position = pos
        self.neighbors = get_neighbors(pos, grid_size)
        self.visited = visited

    def next(self):
        temp = []
        temp.extend(self.visited)
        temp.append(self.position)
        return [ Node(n, self.grid_size, temp) for n in self.neighbors if n not in self.visited]

    def apply(self, initial_state):
        log.debug('Applying path of node traversal on given node : %s', self)
        temp = initial_state.copy()
        first = self.position
        for second in self.visited:
            swap_cell(first, second, temp)
            first = second
        log.debug('State after apply : \n%s', temp)
        return temp

    def __repr__(self):
        return "Position : {}\tVisited : {}\tNeighbors : {}".format(self.position, self.visited, self.neighbors)
