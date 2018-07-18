from str_cube import *
from Queue import Queue as Q
from collections import defaultdict as DD

def bfs_solve(start):
    start = tuple(start)
    if start == tuple(range(54)):
        return
    seen = {start: None}
    q = Q()
    q.put(start)
    end = tuple(range(54))
    while not q.empty():
        c = q.get(False)
        if c == end:
            break
        for n, fd in all_moves(c):
            n = tuple(n)
            if n not in seen:
                seen[n] = (c, fd)
                q.put(n)
    path = []
    n = seen[end]
    while n is not None:
        path.append(n)
        n = seen[n[0]]
    print '\n'.join(map(lambda m: str(m[1]), path[::-1]))

def double_bfs_solve(start):
    start = tuple(start)
    if start == tuple(range(54)):
        return
    end = tuple(range(54))
    seen = ({start: None}, {end: None})

    q = Q()
    q.put((start, 0))
    q.put((end, 1))
    
    while not q.empty():
        c, d = q.get()
        if c in seen[(d+1)%2]:
            break
        for n, fd in all_moves(c):
            n = tuple(n)
            if n not in seen[d]:
                seen[d][n] = (c, fd)
                q.put((n, d))
    path = []
    n = seen[1][c]
    while n is not None:
        n = (n[0], (n[1][0], (n[1][1]+1)%2))
        path.append(n)
        n = seen[1][n[0]]
    print len(path)
    path = path[::-1]
    n = seen[0][c]
    while n is not None:
        path.append(n)
        n = seen[0][n[0]]
    print '\n'.join(map(lambda m: "%s\t%d"%m[1], path[::-1]))
    print len(path)
    

def main():
    c, moves = scramble(range(54), 10)
    print "\n".join(map(lambda m: "%s\t%d"%m, moves))
    print
    double_bfs_solve(c)

if __name__ == "__main__":
    main()
