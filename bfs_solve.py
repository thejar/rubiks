from str_cube import *
from queue import Queue as Q
from collections import defaultdict as DD
import time

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
            print("max_depth exceeded,", len(seen), "states searched")
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
    print('\n'.join(map(lambda m: str(m[1]), path[::-1])))

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
        #print(depth)
        if c in seen[(d+1)%2]:
            break
        if max_depth > 0 and depth-d > max_depth:
            print("max_depth exceeded,", len(seen[0])+len(seen[1]), "states searched")
            return False
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
    path = path[::-1]
    n = seen[0][c]
    while n is not None:
        path.append(n)
        n = seen[0][n[0]]
    #print('\n'.join(map(lambda m: "%s\t%d"%m[1], path[::-1])))
    print(len(path))
    return True
    
def sparse_double_bfs_solve(start, max_depth=-1):
    start = tuple(start)
    if start == tuple(range(54)):
        return
    max_depth /= 2
    end = tuple(range(54))
    seen = ({start: None}, {end: None})

    q = Q()
    q.put((start, 0, 0))
    q.put((end, 1, 0))
    
    i = 0
    while not q.empty():
        c, d, depth = q.get()
        #print(depth)
        if c in seen[(d+1)%2]:
            break
        if depth == 3 and d == 0:
            i += 1
            i %= 1024
            if i != 0:
                continue
        for n, fd in all_moves(c):
            n = tuple(n)
            if n not in seen[d]:
                seen[d][n] = (c, fd)
                if len(seen[d]) % 100000 == 0:
                    print(d, len(seen[d]), depth)
                q.put((n, d, depth+1))
    path = []
    n = seen[1][c]
    while n is not None:
        n = (n[0], (n[1][0], (n[1][1]+1)%2))
        path.append(n)
        n = seen[1][n[0]]
    print(len(path))
    path = path[::-1]
    n = seen[0][c]
    while n is not None:
        path.append(n)
        n = seen[0][n[0]]
    print('\n'.join(map(lambda m: "%s\t%d"%m[1], path[::-1])))
    print(len(path))

def main():
    c, moves = scramble(range(54), 12)
    print("\n".join(map(lambda m: "%s\t%d"%m, moves)))
    print
    t1 = time.time()
    double_bfs_solve(c)
    t2 = time.time()
    print(t2-t1)
    sparse_double_bfs_solve(c)
    t3 = time.time()
    print(t3-t2)
    #bfs_solve(c, 2)

if __name__ == "__main__":
    main()
