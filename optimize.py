from queue import Queue as Q
from collections import defaultdict as DD
import bfs

def opt1(path, neighbors):
    if len(path) < 8:
        return bfs.d_bfs1(path[0], path[1], neighbors)

    new_path = [n for n in path]
    #while len(new_path) > len(old_path):
    start = 0
    while start < len(new_path) - 5:
        end = start + 5
        start_n = new_path[start]
        end_n = new_path[end]
        new_path = new_path[:start] + bfs.d_bfs1(start_n, end_n, neighbors) + new_path[end+1:]
        start += 1
    return new_path

def snip(path):
    new_path = [n for n in path]
    seen = {}
    i = 0
    while i < len(new_path):
        if new_path[i] in seen:
            old = seen[new_path[i]]
            for node in new_path[old+1:i]:
                del seen[node]
            new_path = new_path[:old] + new_path[i:]
            i = old+1
        else:
            seen[new_path[i]] = i
            i += 1
    return new_path

def opt2(path, neighbors):
    new_path = snip(path)

    if len(new_path) < 8:
        return bfs.d_bfs1(path[0], path[1], neighbors)

    start = 0
    while start < len(new_path):
        others = set() #{new_path[i] for i in range(len(new_path)) if abs(i-start) > 5}
        for i in range(len(new_path)):
            print(abs(i-start))
            if abs(i-start) > 5:
                others.add(new_path[i])
        print(start, others)
        segment = bfs.multi_bfs(start, others, neighbors)
        if segment[0] == new_path[start]:
            pos = path.index(segment[-1])
            if len(segment) < pos - start:
                new_path = new_path[:start] + segment + new_path[pos+1:]
        elif segment[-1] == new_path[start]:
            pos = path.index(segment[0])
            if len(segment) < start - pos:
                new_path = new_path[:pos] + segment + new_path[start+1]
        else:
            print("start not at beginning or end of segment?")
            return
        start += 1

def test1():
    nodes = DD(set)
    edges = zip(range(0, 10), range(1, 11))
    for a, b in edges:
        nodes[a] |= {b}
        nodes[b] |= {a}
    
    path = list(range(0, 10)) + list(range(8, 0, -1))
    print(' -> '.join(map(str, path)))
    opt_path = opt2(path, nodes.__getitem__)
    print(' -> '.join(map(str, opt_path)))

def test2():
    nodes = DD(set)
    edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 2),
            (2, 5),
        ]
    for a, b in edges:
        nodes[a] |= {b}
        nodes[b] |= {a}
    
    path = [1, 2, 3, 4, 2, 5]
    print(' -> '.join(map(str, path)))
    opt_path = snip(path)
    print(' -> '.join(map(str, opt_path)))

if __name__ == "__main__":
    test1()
