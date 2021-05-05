import logging

from project.src.state import State
log_format='[%(name)s] : %(message)s'
logging.basicConfig(level=logging.INFO , format=log_format)

log = logging.getLogger('Main')

if __name__ == '__main__':
    log.debug('Initializing search')

    state = State(2)
    print(state)
    queue = [state]
    count = 0
    while queue:
        count+=1
        s = queue.pop(0)
        print("------------------")
        print(s.to_string())
        print("==================")
        
        for n in s.next():
            queue.append(n)

    print(count)
