from collections import defaultdict as DD
from queue import Queue as Q
import random
import sys

def bfs(start, end, neighbors):
    parents = {}
    q = Q()
    # node, depth, parent
    q.put((start, 0, start))
    
    while not q.empty():
        node, depth, parent = q.get(False)
        if node in parents:
            continue
        parents[node] = parent
        if node == end:
            break
        
        for n in neighbors(node):
            if n not in parents:
                q.put((n, depth+1, node))
    
    if end not in parents:
        return False
    path = [end]
    while path[0] != start:
        path = [parents[path[0]]] + path
    return path

def multi_bfs(start, end, neighbors):
    parents = {}
    q = Q()
    # node, depth, parent
    q.put((start, 0, start))
    last = None
    
    while not q.empty():
        node, depth, parent = q.get(False)
        if node in parents:
            continue
        parents[node] = parent
        if node in end:
            last = node
            break
        
        for n in neighbors(node):
            if n not in parents:
                q.put((n, depth+1, node))
    
    path = [last]
    while path[0] != start:
        path = [parents[path[0]]] + path
    return path

def d_bfs(start, end, neighbors):
    if start == end:
        return [start]

    a_prev = {}
    b_prev = {}
    path = None

    a_q = Q()
    b_q = Q()
    a_q.put((start, 0, start))
    b_q.put((end, 0, end))

    while not (a_q.empty() or b_q.empty()):
        
        node, depth, parent = a_q.get(False)
        if node not in a_prev:
            a_prev[node] = parent
            if node == end or node in b_prev:
                path = [parent, node]
                break
            for n in neighbors(node):
                if n not in a_prev:
                    a_q.put((n, depth+1, node))

        node, depth, parent = b_q.get(False)
        if node not in b_prev:
            b_prev[node] = parent
            if node == start or node in a_prev:
                path = [node, parent]
                break
            for n in neighbors(node):
                if n not in b_prev:
                    b_q.put((n, depth+1, node))
        
    if path is None:
        return False

    while path[-1] != end:
        path += [b_prev[path[-1]]]
    while path[0] != start:
        path = [a_prev[path[0]]] + path
    return path

def d_bfs1(start, end, neighbors):
    if start == end:
        return [start]

    prev = {}
    path = None

    q = Q()
    q.put((start, 0, start, True))
    q.put((end, 0, end, False))

    while not q.empty():
        
        node, depth, parent, d = q.get(False)
        if node not in prev:
            prev[node] = (parent, d)
            for n in neighbors(node):
                q.put((n, depth+1, node, d))
        if prev[node][-1] is not d:
            if d:
                path = [parent, node]
            else:
                path = [node, parent]
            break

    if path is None:
        return False

    while path[-1] != end:
        path += [prev[path[-1]][0]]
    while path[0] != start:
        path = [prev[path[0]][0]] + path
    return path

def test():
    nodes = DD(set)
    #n = 10000
    #e = 15000
    #a, b = None, None
    #for _ in range(e):
    #    while a == b or a in nodes[b]:
    #        a = random.randint(0, n)
    #        b = random.randint(0, n)
    #    nodes[a] |= {b}
    #    nodes[b] |= {a}
    edges = [
            (0, 5),
            (5, 1),
            (5, 6),
            (6, 1),
            (6, 2),
        ]
    for a, b in edges:
        nodes[a] |= {b}
        nodes[b] |= {a}
    path = multi_bfs(0, {2}, nodes.__getitem__)
    if not path:
        print("No path found")
    else:
        print(" -> ".join(map(str, path)))

if __name__ == "__main__":
    seed = random.randint(0, 1000000000)
    if len(sys.argv) > 1:
        seed = int(sys.argv[1])
    print("seed:", seed)
    random.seed(seed)

    #for t in range(1000):
    test()
        #if (t+1) % 100 == 0:
            #print(t+1)
