from str_cube import *
from Queue import Queue as Q
from collections import defaultdict as DD

def bfs_solve(start, max_depth=-1):
    start = tuple(start)
    if start == tuple(range(54)):
        return
    seen = {start: None}
    q = Q()
    q.put((start, 0))
    end = tuple(range(54))
    while not q.empty():
        c, depth = q.get(False)
        if c == end:
            break
        if max_depth > 0 and depth > max_depth:
            print "max_depth exceeded,", len(seen), "states searched"
            return
        for n, fd in all_moves(c):
            n = tuple(n)
            if n not in seen:
                seen[n] = (c, fd)
                q.put((n, depth+1))
    path = []
    n = seen[end]
    while n is not None:
        path.append(n)
        n = seen[n[0]]
    print '\n'.join(map(lambda m: str(m[1]), path[::-1]))

def double_bfs_solve(start, max_depth=-1):
    start = tuple(start)
    if start == tuple(range(54)):
        return
    max_depth /= 2
    end = tuple(range(54))
    seen = ({start: None}, {end: None})

    q = Q()
    q.put((start, 0, 0))
    q.put((end, 1, 0))
    
    while not q.empty():
        c, d, depth = q.get()
        #print depth
        if c in seen[(d+1)%2]:
            break
        if max_depth > 0 and depth-d > max_depth:
            print "max_depth exceeded,", len(seen[0])+len(seen[1]), "states searched"
            return
        for n, fd in all_moves(c):
            n = tuple(n)
            if n not in seen[d]:
                seen[d][n] = (c, fd)
                q.put((n, d, depth+1))
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
    #bfs_solve(c)

if __name__ == "__main__":
    main()
