from str_cube import *

def jeff_solve(c):
    def white_cross(c):
        from_p_to_front = {
                1: [BACK_RIGHT, TOP_LEFT, TOP_LEFT, BACK_LEFT, TOP_LEFT, TOP_LEFT],
                3: [LEFT_DOWN, TOP_LEFT, LEFT_UP, TOP_RIGHT],
                5: [RIGHT_DOWN, TOP_RIGHT, RIGHT_UP, TOP_LEFT],
                7: [],
                10: [FRONT_RIGHT, TOP_RIGHT, RIGHT_UP, TOP_LEFT],
                12: [TOP_LEFT, LEFT_UP, TOP_RIGHT],
                14: [TOP_RIGHT, RIGHT_UP, TOP_LEFT],
                16: [BOTTOM_RIGHT, RIGHT_UP, FRONT_LEFT, RIGHT_DOWN],
                19: [TOP_RIGHT, TOP_RIGHT, BACK_LEFT, TOP_LEFT, TOP_LEFT],
                21: [RIGHT_DOWN, FRONT_LEFT],
                23: [RIGHT_UP, FRONT_LEFT, RIGHT_DOWN],
                25: [FRONT_LEFT],
                28: [FRONT_LEFT, FRONT_LEFT],
                30: [BOTTOM_RIGHT, FRONT_LEFT, FRONT_LEFT],
                32: [BOTTOM_LEFT, FRONT_LEFT, FRONT_LEFT],
                34: [BOTTOM_LEFT, BOTTOM_LEFT, FRONT_LEFT, FRONT_LEFT],
                37: [BOTTOM_LEFT, RIGHT_UP, FRONT_LEFT, RIGHT_DOWN],
                39: [TOP_LEFT, LEFT_DOWN, TOP_RIGHT],
                41: [TOP_RIGHT, RIGHT_DOWN, TOP_LEFT],
                43: [TOP_LEFT, RIGHT_DOWN, TOP_RIGHT, FRONT_LEFT],
                46: [TOP_LEFT, TOP_LEFT, BACK_RIGHT, TOP_LEFT, TOP_LEFT],
                48: [LEFT_UP, FRONT_RIGHT, LEFT_DOWN],
                50: [LEFT_DOWN, FRONT_RIGHT],
                52: [FRONT_RIGHT],
            }
        for p in [7, 5, 1, 3]:
            loc = find_piece(c, p)
            moves = from_p_to_front[loc]
            c = make_moves(moves, c)
            c = make_shift("side", 1, c)
        return c
            
    def white_corners(c):
        from_p_to_corner = {
                0: [LEFT_UP, RIGHT_DOWN, BOTTOM_LEFT, BOTTOM_LEFT, RIGHT_UP, LEFT_DOWN],
                2: [BACK_RIGHT, BOTTOM_LEFT, BOTTOM_LEFT, BACK_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                6: [LEFT_DOWN, BOTTOM_RIGHT, LEFT_UP, RIGHT_DOWN, BOTTOM_LEFT, RIGHT_UP],
                8: [],
                9: [LEFT_DOWN, BOTTOM_LEFT, LEFT_UP, BOTTOM_LEFT, FRONT_RIGHT, BOTTOM_LEFT, BOTTOM_LEFT, FRONT_LEFT],
                11: [RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                15: [BOTTOM_RIGHT, RIGHT_DOWN, BOTTOM_LEFT, RIGHT_UP],
                17: [BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                18: [RIGHT_UP, BOTTOM_RIGHT, RIGHT_UP, RIGHT_UP, BOTTOM_LEFT, BOTTOM_LEFT, RIGHT_UP],
                20: [BOTTOM_RIGHT, RIGHT_DOWN, BOTTOM_LEFT, BOTTOM_LEFT, RIGHT_UP],
                24: [RIGHT_DOWN, BOTTOM_LEFT, RIGHT_UP, BOTTOM_RIGHT, RIGHT_DOWN, BOTTOM_LEFT, RIGHT_UP],
                26: [BOTTOM_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT],
                27: [BOTTOM_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT, RIGHT_DOWN, BOTTOM_LEFT, BOTTOM_LEFT, RIGHT_UP],
                29: [RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP, FRONT_RIGHT, BOTTOM_LEFT, BOTTOM_LEFT, FRONT_LEFT],
                33: [BOTTOM_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP, FRONT_RIGHT, BOTTOM_LEFT, BOTTOM_LEFT, FRONT_LEFT],
                35: [BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP, FRONT_RIGHT, BOTTOM_LEFT, BOTTOM_LEFT, FRONT_LEFT],
                36: [RIGHT_DOWN, BOTTOM_LEFT, BOTTOM_LEFT, RIGHT_UP],
                38: [FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT],
                42: [RIGHT_DOWN, BACK_LEFT, BOTTOM_LEFT, BOTTOM_LEFT, BACK_RIGHT, RIGHT_UP],
                44: [BACK_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, BACK_LEFT, FRONT_LEFT],
                45: [FRONT_RIGHT, BOTTOM_LEFT, BOTTOM_LEFT, FRONT_LEFT],
                47: [LEFT_UP, FRONT_RIGHT, BOTTOM_LEFT, BOTTOM_LEFT, FRONT_LEFT, LEFT_DOWN],
                51: [RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                53: [LEFT_DOWN, RIGHT_DOWN, BOTTOM_RIGHT, LEFT_UP, RIGHT_UP],
            }
        for p in [8, 2, 0, 6]:
            loc = find_piece(c, p)
            moves = from_p_to_corner[loc]
            c = make_moves(moves, c)
            c = make_shift("side", 1, c)
        return c

    def side_edges(c):
        from_p_to_edge = {
                12: [LEFT_DOWN, BOTTOM_LEFT, LEFT_UP, BOTTOM_LEFT, FRONT_LEFT, BOTTOM_RIGHT, FRONT_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                14: [],
                16: [BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP, BOTTOM_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT],
                19: [BACK_RIGHT, BOTTOM_RIGHT, BACK_LEFT, BOTTOM_RIGHT, RIGHT_UP, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_LEFT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                23: [BOTTOM_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP, BOTTOM_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT],
                25: [RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP, BOTTOM_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT, BOTTOM_RIGHT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP, BOTTOM_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT],
                28: [BOTTOM_LEFT, BOTTOM_LEFT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                30: [BOTTOM_LEFT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                32: [BOTTOM_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                34: [FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                37: [BOTTOM_RIGHT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP, BOTTOM_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT],
                39: [LEFT_UP, BOTTOM_RIGHT, LEFT_DOWN, BOTTOM_RIGHT, BACK_LEFT, BOTTOM_LEFT, BACK_RIGHT, BOTTOM_LEFT, BOTTOM_LEFT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                41: [RIGHT_UP, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_LEFT, BACK_RIGHT, BOTTOM_RIGHT, BACK_LEFT, BOTTOM_LEFT, BOTTOM_LEFT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                46: [BACK_LEFT, BOTTOM_LEFT, BACK_RIGHT, BOTTOM_LEFT, LEFT_UP, BOTTOM_RIGHT, LEFT_DOWN, BOTTOM_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
                48: [RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP, BOTTOM_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT],
                52: [FRONT_LEFT, BOTTOM_RIGHT, FRONT_RIGHT, BOTTOM_RIGHT, LEFT_DOWN, BOTTOM_LEFT, LEFT_UP, BOTTOM_RIGHT, FRONT_RIGHT, BOTTOM_LEFT, FRONT_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP],
            }
        for p in [14, 19, 39, 52]:
            #print(p)
            #print(display(c))
            #print()
            loc = find_piece(c, p)
            #print(loc)
            moves = from_p_to_edge[loc]
            c = make_moves(moves, c)
            #print(display(c))
            #print()
            #print("--------------------------")
            c = make_shift("side", 1, c)
        return c

    def yellow_cross(c):
        s = 0
        cold = color_cube(c)
        if cold[28] == 'y' and cold[30] == 'y' and cold[32] == 'y' and cold[34] == 'y':
            return c
        if cold[30] == 'y' and cold[32] == 'y':
            c = make_shift("side", 1, c)
            s = 1
        if s == 1 or (cold[28] == 'y' and cold[34] == 'y'):
            moves = [RIGHT_DOWN, BACK_RIGHT, BOTTOM_LEFT, BACK_LEFT, BOTTOM_RIGHT, RIGHT_UP]
            c = make_moves(moves, c)
            if s == 1:
                c = make_shift("side", 0, c)
            return c
        if cold[28] == 'y':
            if cold[32] == 'y':
                c = make_shift("side", 1, c)
                s = 1
            moves = [RIGHT_DOWN, BOTTOM_LEFT, BACK_RIGHT, BOTTOM_RIGHT, BACK_LEFT, RIGHT_UP]
            c = make_moves(moves, c)
            if s == 1:
                c = make_shift("side", 0, c)
            return c
        if cold[34] == 'y':
            if cold[32] == 'y':
                c = make_shift("side", 0, c)
                s = 1
            moves = [FRONT_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP, FRONT_RIGHT]
            c = make_moves(moves, c)
            if s == 1:
                c = make_shift("side", 1, c)
            return c
        moves = [FRONT_LEFT, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, RIGHT_UP, FRONT_RIGHT]
        c = make_moves(moves, c)
        moves = [RIGHT_DOWN, BACK_RIGHT, BOTTOM_LEFT, BACK_LEFT, BOTTOM_RIGHT, RIGHT_UP]
        c = make_moves(moves, c)
        return c

    def bottom_edges(c):
        pass
    def yellow_corner_permutation(c):
        pass
    def yellow_corner_orientation(c):
        pass
    
    c = white_cross(c)
    print("stage 1")
    print(display(color_cube(c)))
    c = white_corners(c)
    print("stage 2")
    print(display(color_cube(c)))
    c = side_edges(c)
    print("stage 3")
    print(display(color_cube(c)))
    c = yellow_cross(c)
    print("stage 4")
    print(display(color_cube(c)))
    #c = bottom_edges(c)
    #c = yellow_corner_permutation(c)
    #c = yellow_corner_orientation(c)
    
c, moves = scramble(range(54))
jeff_solve(c)
