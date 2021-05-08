import logging

from project.src.search import Search
from project.src.state import State
from project.src.heuristic import *
from project.src.puzzle import create_puzzle, Puzzle

log_format='[%(name)s] : %(message)s'
logging.basicConfig(level=logging.DEBUG , format=log_format)

log = logging.getLogger('Main')

if __name__ == '__main__':
    log.debug('Initializing search')

    puz = create_puzzle(3)
    state = State(puz, None)
    visited = []
    bfs = [state]
    count = 0
    search = Search(3)
    print(search.solve(state, manhattan_distance))
#    new_puz = Puzzle([4,0,8,6,1,3,5,7,2], (0,1), (3,3))
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
