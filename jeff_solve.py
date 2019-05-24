from str_cube import *
from bfs_solve import double_bfs_solve

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
            loc = find_piece(c, p)
            moves = from_p_to_edge[loc]
            c = make_moves(moves, c)
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
        rotate_tri = [RIGHT_DOWN, BOTTOM_LEFT, RIGHT_UP, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, BOTTOM_RIGHT, RIGHT_UP]
        while c[16] != 16:
            c = make_move(*BOTTOM_RIGHT, c)
        if c[23] == 23:
            if c[37] == 37:
                return c
            c = make_move(*BOTTOM_LEFT, c)
            c = make_shifts([("side", 0)] * 2, c)
            c = make_moves(rotate_tri, c)
            c = make_shifts([("side", 0)] * 2, c)
            return c
        if c[48] == 48:
            c = make_move(*BOTTOM_RIGHT, c)
            c = make_shifts([("side", 0)] * 2, c)
            c = make_moves(rotate_tri*2, c)
            c = make_shifts([("side", 0)] * 2, c)
            return c
        if c[37] == 37:
            c = make_moves(rotate_tri, c)
            c = make_move(*BOTTOM_LEFT, c)
            c = make_shifts([("side", 0)] * 2, c)
            c = make_moves(rotate_tri, c)
            c = make_shifts([("side", 0)] * 2, c)
            return c
        c = make_moves(rotate_tri, c)
        if c[23] == 23:
            return c
        c = make_moves(rotate_tri, c)
        return c

    def yellow_corner_permutation(c):
        perm_f = [RIGHT_DOWN, BOTTOM_RIGHT, LEFT_DOWN, BOTTOM_LEFT, RIGHT_UP, BOTTOM_RIGHT, LEFT_UP, BOTTOM_LEFT]
        perm_b = [LEFT_DOWN, BOTTOM_LEFT, RIGHT_DOWN, BOTTOM_RIGHT, LEFT_UP, BOTTOM_LEFT, RIGHT_UP, BOTTOM_RIGHT]
        #print(display(c))
        s_corner = i_CORNERS[find_piece(c, 15)][0]
        #print(s_corner)
        if s_corner == 15:
            # great
            pass
        elif s_corner == 17:
            c = make_moves(perm_f + perm_b, c)
        elif s_corner == 20:
            c = make_moves(perm_b, c)
        elif s_corner == 33:
            c = make_moves(perm_b * 2, c)
        else:
            print("Error, corner in unexpected place!", s_corner)
        #print(display(c))
        #input(":")

        # tl corner is in place
        while i_CORNERS[find_piece(c, 17)][0] != 17:
            c = make_moves(perm_f, c)
            #print(find_piece(c, 17))
            #print(display(c))
            #input(":")

        return c
    def yellow_corner_orientation(c):
        orient_f = [LEFT_UP, TOP_LEFT, LEFT_DOWN, TOP_RIGHT, LEFT_UP, TOP_LEFT, LEFT_DOWN]
        orient_b = [LEFT_UP, TOP_RIGHT, LEFT_DOWN, TOP_LEFT, LEFT_UP, TOP_RIGHT, LEFT_DOWN]

        last = 'c'
        
        if c[15] == 51: # y
            c = make_moves(orient_b, c)
            last += 'b'
        elif c[15] == 27:
            c = make_moves(orient_f, c)
            last += 'f'
        c = make_move(*BOTTOM_LEFT, c)
        
        if c[15] == 17:
            if last[-1] == 'b':
                c = make_move(*TOP_LEFT, c)
            last += 'b'
            c = make_moves(orient_b, c)
        elif c[15] == 29: # y
            if last[-1] == 'f':
                c = make_move(*TOP_RIGHT, c)
            last += 'f'
            c = make_moves(orient_f, c)
        c = make_move(*BOTTOM_LEFT, c)
        
        if c[15] == 20:
            if last[-1] == 'b':
                c = make_move(*TOP_LEFT, c)
            last += 'b'
            c = make_moves(orient_b, c)
        elif c[15] == 35: # y
            if last[-1] == 'f':
                c = make_move(*TOP_RIGHT, c)
            last += 'f'
            c = make_moves(orient_f, c)
        c = make_move(*BOTTOM_LEFT, c)
        
        if c[15] == 36:
            if last[-1] == 'b':
                c = make_move(*TOP_LEFT, c)
            last += 'b'
            c = make_moves(orient_b, c)
        elif c[15] == 33: # y
            if last[-1] == 'f':
                c = make_move(*TOP_RIGHT, c)
            last += 'f'
            c = make_moves(orient_f, c)
        c = make_move(*BOTTOM_LEFT, c)
        while c[0] != 0:
            c = make_move(*TOP_LEFT, c)
        return c

    clear_moves()
    
    mask = ["*"]*54
    for i in [4, 13, 22, 31, 40, 49]:
        mask[i] = '-'

    if not match(mask, c):
        print("mismatch!")
        print(display(c))
        return

    print(display(color_cube(c)))

    c = white_cross(c)
    for i in [1, 3, 5, 7, 10, 21, 43, 50]:
        mask[i] = '-'
    if not match(mask, c):
        print("stage 1")
        print("mismatch!")
        print(display(c))
        return

    c = white_corners(c)
    for i in [0, 2, 6, 8, 9, 11, 18, 24, 42, 44, 47, 53]:
        mask[i] = '-'
    if not match(mask, c):
        print("stage 2")
        print("mismatch!")
        print(display(c))
        return

    c = side_edges(c)
    for i in [12, 14, 19, 25, 39, 41, 46, 52]:
        mask[i] = '-'
    if not match(mask, c):
        print("stage 3")
        print("mismatch!")
        print(display(c))
        return

    c = yellow_cross(c)
    for i in [28, 30, 32, 34]:
        mask[i] = 'c'
    if not match(mask, c):
        print("stage 4")
        print("mismatch!")
        print(display(c))
        return

    c = bottom_edges(c)
    for i in [16, 23, 28, 30, 32, 34, 37, 48]:
        mask[i] = '-'
    if not match(mask, c):
        print("stage 5")
        print("mismatch!")
        print(display(c))
        return

    c = yellow_corner_permutation(c)
    #print("stage 6")
    #print(display(color_cube(c)))
    #print(display(c))
    #for i in [16, 23, 28, 30, 32, 34, 37, 48]:
    #    mask[i] = '-'
    #if not match(mask, c):
    #    print("mismatch!")
    #    print(display(c))
    #    return

    c = yellow_corner_orientation(c)
    print("solved!")
    print(display(color_cube(c)))
    #print('\n'.join(map(str, moves_made)))
    print(len(moves_made))
    if not match('-'*54, c):
        print("mismatch!")
        print(display(c))
        return

    
c, moves = scramble(range(54))

if not double_bfs_solve(c, 8):
    jeff_solve(c)
