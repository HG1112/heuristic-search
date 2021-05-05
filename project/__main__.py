import numpy as np
import logging

from project.src.node import Node
from project.src.search import Search
from project.src.heuristic import no_cost, manhatten_distance , misplaced_tile

log_format='[%(name)s] : %(message)s'
logging.basicConfig(level=logging.INFO , format=log_format)

log = logging.getLogger('Main')

if __name__ == '__main__':
    log.debug('Initializing search')

    goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
    #initial_state = np.array([[1,2,3], [4,0,6], [7,5,8]])
    #node = Node((1,1), 3, [(2,2), (2,1)])
    #actual = node.apply(initial_state)
    #print(actual)
    initial_state = np.array([[1,2,3], [0,5,6], [4,7,8]])
    search = Search(goal_state) 
    result = search.find( initial_state , no_cost)
    print('Initial: \n{}'.format(initial_state))
    print('Result: \n{}'.format(result))
    print('Result Apply : \n{}'.format(result.apply(initial_state)))

#puzzle = np.array([[1,2,3], [4,5,6], [7,8,0]])
#goal_state = puzzle
#puzzle = np.array([[1,2,3], [4,0,6], [7,5,8]])
#initial_state = puzzle


