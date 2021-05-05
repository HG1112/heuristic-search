def get_neighbors(position, grid_size):
    x = position[0]
    y = position[1]
    return [ (i,j) for (i,j) in [(x+1,y), (x-1, y), (x, y+1), (x, y-1)] if i >= 0 and j >= 0 and i < grid_size and j < grid_size]

def swap_cell(pos1, pos2, state):
    x1 = pos1[0]
    x2 = pos2[0]
    y1 = pos1[1]
    y2 = pos2[1]
    if abs(x1+y1-x2-y2) == 1:
        state[x1][y1] , state[x2][y2] = state[x2][y2], state[x1][y1]
    else:
        raise ValueError('Unsupported swap of cells between {} and {}'.format(pos1, pos2))

