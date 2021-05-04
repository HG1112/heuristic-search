import numpy as np
import logging

from node import Node
from search import Search
from heuristic import no_cost, manhatten_distance , misplaced_tile

log_format='[%(name)s] : %(message)s'
logging.basicConfig(level=logging.DEBUG , format=log_format)

log = logging.getLogger('Heuristic Search')

#puzzle = np.array([[1,2,3], [4,5,6], [7,8,0]])
#goal_state = puzzle
#puzzle = np.array([[1,2,3], [4,0,6], [7,5,8]])
#initial_state = puzzle

#log.info('Initializing search')
#search = Search(goal_state) 
#result = search.find( initial_state , no_cost)
#print(result)
#print(result.apply(goal_state))
#print(initial_state)

goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
initial_state = np.array([[1,2,3], [4,0,6], [7,5,8]])
node = Node((1,1), 3, [(2,2), (2,1)])
actual = node.apply(initial_state)
print(actual)
