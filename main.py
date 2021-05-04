from search import Search
from node import Node
import numpy as np
import logging

log_format='[%(name)s] : %(message)s'
logging.basicConfig(level=logging.INFO , format=log_format)


log = logging.getLogger('Heuristic Search')

puzzle = np.array([[1,2,3], [4,5,6], [7,8,0]])
goal_state = puzzle
puzzle = np.array([[1,2,3], [4,0,6], [7,5,8]])
initial_state = puzzle

log.info('Initializing search')
search = Search((1,1), initial_state, goal_state, None) 
print(search.find())

#node = Node((2,2), 3, [])
#for n in node.next():
#    print(n)
