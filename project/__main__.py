import logging
from random import random

from project.src.search import Search
from project.src.state import State
from project.src.heuristic import *
from project.src.puzzle import create_puzzle, Puzzle

log_format='[%(name)s] : %(message)s'
logging.basicConfig(level=logging.INFO , format=log_format)

log = logging.getLogger('Main')

if __name__ == '__main__':
    log.debug('Initializing search')

    #new_puz = Puzzle([4,0,8,6,1,3,5,7,2], (0,1), (3,3))
    #new_puz = Puzzle([4,8,0,6,1,3,5,7,2], (0,2), (3,3))
    #new_puz = Puzzle([ 1, 6, 7, 5, 0, 3, 4, 8, 2], (1,1), (3,3))
    #new_puz = Puzzle([1,3,0,4,2,5,7,8,6], (0,2), (3,3))
    #new_puz = Puzzle([2,6,7,3,0,1,11,4,5,14,10,8,9,13,15,12], (1,0), (4,4))
    new_puz = Puzzle([2,5,7,3,1,6,11,4,9,0,15,8,13,10,14,12], (2, 1), (4,4))
    state = State(new_puz, None)
    search = Search(4)
    result = search.solve(state, manhattan_distance)
    print('Path: \n',result.path_from_root())
    print('Cost : ', result.depth)
    print('Solution: ')
    while result:
        print(result.puzzle)
        result = result.parent
    #depth = 15
    #while True:
        #new_puz = Puzzle([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0], (3,3), (4,4))
        #state = State(new_puz, None)
        #visited = [new_puz]
        #for i in range(0, depth):
            #next = state.next_possible_states(visited)
            #index = int((len(next) -1)*random())
            #state = next[index]
        #state.parent = None
        #search1 = Search(4)
        #result1 = search1.solve(state, misplaced_tile)
        #print('Path: \n',result1.path_from_root())
        #print('Depth : ', result1.depth)
        #search2 = Search(4)
        #result2 = search2.solve(state, manhattan_distance)
        #print('Path: \n',result2.path_from_root())
        #print('Depth : ', result2.depth)
        #if result2.path_from_root() != result1.path_from_root():
            #print('Puzzle: ', state.puzzle)
            #break
#    while bfs:
#        s = bfs.pop(-1)
#        if s.puzzle == new_puz:
#            print ('ans :', s.puzzle)
#            break
#        count += 1
#        print(count)
#        if s.puzzle not in visited:
#            sts = s.next_possible_states(visited)
#            print(len(sts))
#            for st in sts:
#                print(st.puzzle)
#                bfs.append(st)
#            visited.append(s.puzzle)
