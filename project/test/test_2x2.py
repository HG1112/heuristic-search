from project.src.state import State

def test_2x2():
    bfs = [ State(2) ]
    count = 0
    while bfs:
        count+=1
        s = bfs.pop(0)
        for n in s.next():
            bfs.append(n)
    assert count == 23

