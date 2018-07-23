from str_cube import *

cycle = [
        ("left", 1),
        ("bottom", 0),
        ("right", 1),
        ("back", 1),
        ("top", 1),
        ("front", 1)]

c = range(54)

for i in xrange(9):
    for j in xrange(8):
        c = make_moves(cycle, c)
    print i
    print displayc(c)
    print
    print
