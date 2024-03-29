import random
import sys
if len(sys.argv) == 1:
    seed = random.randint(0, 1000000000)
else:
    seed = int(sys.argv[1])
print("seed:", seed)
random.seed(seed)

colors = ('w', 'o', 'g', 'y', 'r', 'b')
TOP = 0
FRONT = 1
RIGHT = 2
BOTTOM = 3
BACK = 4
LEFT = 5
"""       36 37 38
          39 40 41
          42 43 44
       
45 46 47  00 01 02  18 19 20
48 49 50  03 04 05  21 22 23
51 52 53  06 07 08  24 25 26

          09 10 11
          12 13 14
          15 16 17
   
          27 28 29
          30 31 32
          33 34 35
"""

SOLVED_c = ''.join(c*9 for c in colors)

def color_cube(c):
    return ''.join([colors[int(i/9)] for i in c])

def display(c):
    return """          {36:>2} {37:>2} {38:>2}
          {39:>2} {40:>2} {41:>2}
          {42:>2} {43:>2} {44:>2}
       
{45:>2} {46:>2} {47:>2}  {0:>2} {1:>2} {2:>2}  {18:>2} {19:>2} {20:>2}
{48:>2} {49:>2} {50:>2}  {3:>2} {4:>2} {5:>2}  {21:>2} {22:>2} {23:>2}
{51:>2} {52:>2} {53:>2}  {6:>2} {7:>2} {8:>2}  {24:>2} {25:>2} {26:>2}

          {9:>2} {10:>2} {11:>2}
          {12:>2} {13:>2} {14:>2}
          {15:>2} {16:>2} {17:>2}
   
          {27:>2} {28:>2} {29:>2}
          {30:>2} {31:>2} {32:>2}
          {33:>2} {34:>2} {35:>2}""".format(*c)

def displayc(c):
    return display(color_cube(c))

CORNERS = {(0, 42, 47), (2, 18, 44), (6, 9, 53), (8, 11, 24),
        (15, 27, 51), (17, 26, 29), (20, 35, 38), (33, 36, 45)}
i_CORNERS = {}
for a, b, c in CORNERS:
    i_CORNERS[a] = (a, b, c)
    i_CORNERS[b] = (a, b, c)
    i_CORNERS[c] = (a, b, c)

SHIFTS = {
    'vert': [[
        9 , 10, 11, 12, 13, 14, 15, 16, 17,
        27, 28, 29, 30, 31, 32, 33, 34, 35,
        24, 21, 18, 25, 22, 19, 26, 23, 20,
        36, 37, 38, 39, 40, 41, 42, 43, 44,
        0 ,  1,  2,  3,  4,  5,  6,  7,  8,
        47, 50, 53, 46, 49, 52, 45, 48, 51], [
        36, 37, 38, 39, 40, 41, 42, 43, 44,
        0 ,  1,  2,  3,  4,  5,  6,  7,  8,
        20, 23, 26, 19, 22, 25, 18, 21, 24,
        9 , 10, 11, 12, 13, 14, 15, 16, 17,
        27, 28, 29, 30, 31, 32, 33, 34, 35,
        51, 48, 45, 52, 49, 46, 53, 50, 47]],
    'side': [[
        2 ,  5,  8,  1,  4,  7,  0,  3,  6,
        47, 50, 53, 46, 49, 52, 45, 48, 51,
        11, 14, 17, 10, 13, 16,  9, 12, 15,
        33, 30, 27, 34, 31, 28, 35, 32, 29,
        20, 23, 26, 19, 22, 25, 18, 21, 24,
        38, 41, 44, 37, 40, 43, 36, 39, 42], [
        6 ,  3,  0,  7,  4,  1,  8,  5,  2,
        24, 21, 18, 25, 22, 19, 26, 23, 20,
        42, 39, 36, 43, 40, 37, 44, 41, 38,
        29, 32, 35, 28, 31, 34, 27, 30, 33,
        51, 48, 45, 52, 49, 46, 53, 50, 47,
        15, 12,  9, 16, 13, 10, 17, 14, 11]]}

def make_shift(f, d, c):
    return [c[i] for i in SHIFTS[f][d]]

def make_shifts(shift_lst, c):
    for f, d in shift_lst:
        c = make_shift(f, d, c)
    return c

def make_shifts_rev(shift_list, c):
    return make_shifts([(m[0], (m[1]+1)%2) for m in shift_list[::-1]], c)

def all_shifts(c):
    for f in SHIFTS:
        yield make_shift(f, 0, c), (f, 0)
        yield make_shift(f, 1, c), (f, 1)

def random_shift(c):
    f, d = random.sample(MOVES.keys(), 1)[0], random.randint(0, 1)
    return make_shift(f, d, c), (f, d)

MOVES = {
    'right': [[
        0 ,  1, 11,  3,  4, 14,  6,  7, 17,
        9 , 10, 29, 12, 13, 32, 15, 16, 35,
        24, 21, 18, 25, 22, 19, 26, 23, 20,
        27, 28, 38, 30, 31, 41, 33, 34, 44,
        36, 37,  2, 39, 40,  5, 42, 43,  8,
        45, 46, 47, 48, 49, 50, 51, 52, 53], [
        0 ,  1, 38,  3,  4, 41,  6,  7, 44,
        9 , 10,  2, 12, 13,  5, 15, 16,  8,
        20, 23, 26, 19, 22, 25, 18, 21, 24,
        27, 28, 11, 30, 31, 14, 33, 34, 17,
        36, 37, 29, 39, 40, 32, 42, 43, 35,
        45, 46, 47, 48, 49, 50, 51, 52, 53]],
    'left': [[
        9 ,  1,  2, 12,  4,  5, 15,  7,  8,
        27, 10, 11, 30, 13, 14, 33, 16, 17,
        18, 19, 20, 21, 22, 23, 24, 25, 26,
        36, 28, 29, 39, 31, 32, 42, 34, 35,
        0 , 37, 38,  3, 40, 41,  6, 43, 44,
        47, 50, 53, 46, 49, 52, 45, 48, 51], [
        36,  1,  2, 39,  4,  5, 42,  7,  8,
        0 , 10, 11,  3, 13, 14,  6, 16, 17,
        18, 19, 20, 21, 22, 23, 24, 25, 26,
        9 , 28, 29, 12, 31, 32, 15, 34, 35,
        27, 37, 38, 30, 40, 41, 33, 43, 44,
        51, 48, 45, 52, 49, 46, 53, 50, 47]],
    'top': [[
        2 ,  5,  8,  1,  4,  7,  0,  3,  6,
        47, 50, 53, 12, 13, 14, 15, 16, 17,
        11, 19, 20, 10, 22, 23,  9, 25, 26,
        27, 28, 29, 30, 31, 32, 33, 34, 35,
        36, 37, 38, 39, 40, 41, 18, 21, 24,
        45, 46, 44, 48, 49, 43, 51, 52, 42], [
        6 ,  3,  0,  7,  4,  1,  8,  5,  2,
        24, 21, 18, 12, 13, 14, 15, 16, 17,
        42, 19, 20, 43, 22, 23, 44, 25, 26,
        27, 28, 29, 30, 31, 32, 33, 34, 35,
        36, 37, 38, 39, 40, 41, 53, 50, 47,
        45, 46,  9, 48, 49, 10, 51, 52, 11]],
    'bottom': [[
        0 ,  1,  2,  3,  4,  5,  6,  7,  8,
        9 , 10, 11, 12, 13, 14, 45, 48, 51,
        18, 19, 17, 21, 22, 16, 24, 25, 15,
        33, 30, 27, 34, 31, 28, 35, 32, 29,
        20, 23, 26, 39, 40, 41, 42, 43, 44,
        38, 46, 47, 37, 49, 50, 36, 52, 53], [
        0 ,  1,  2,  3,  4,  5,  6,  7,  8,
        9 , 10, 11, 12, 13, 14, 26, 23, 20,
        18, 19, 36, 21, 22, 37, 24, 25, 38,
        29, 32, 35, 28, 31, 34, 27, 30, 33,
        51, 48, 45, 39, 40, 41, 42, 43, 44,
        15, 46, 47, 16, 49, 50, 17, 52, 53]],
    'front': [[
        0 ,  1,  2,  3,  4,  5, 51, 52, 53,
        15, 12,  9, 16, 13, 10, 17, 14, 11,
        18, 19, 20, 21, 22, 23,  6,  7,  8,
        26, 25, 24, 30, 31, 32, 33, 34, 35,
        36, 37, 38, 39, 40, 41, 42, 43, 44,
        45, 46, 47, 48, 49, 50, 29, 28, 27], [
        0 ,  1,  2,  3,  4,  5, 24, 25, 26,
        11, 14, 17, 10, 13, 16,  9, 12, 15,
        18, 19, 20, 21, 22, 23, 29, 28, 27,
        53, 52, 51, 30, 31, 32, 33, 34, 35,
        36, 37, 38, 39, 40, 41, 42, 43, 44,
        45, 46, 47, 48, 49, 50,  6,  7,  8]],
    'back': [[
        45, 46, 47,  3,  4,  5,  6,  7,  8,
        9 , 10, 11, 12, 13, 14, 15, 16, 17,
        0 ,  1,  2, 21, 22, 23, 24, 25, 26,
        27, 28, 29, 30, 31, 32, 20, 19, 18,
        38, 41, 44, 37, 40, 43, 36, 39, 42,
        35, 34, 33, 48, 49, 50, 51, 52, 53], [
        18, 19, 20,  3,  4,  5,  6,  7,  8,
        9 , 10, 11, 12, 13, 14, 15, 16, 17,
        35, 34, 33, 21, 22, 23, 24, 25, 26,
        27, 28, 29, 30, 31, 32, 47, 46, 45,
        42, 39, 36, 43, 40, 37, 44, 41, 38,
        0 ,  1,  2, 48, 49, 50, 51, 52, 53]]}

RIGHT_UP = ("right", 0)
RIGHT_DOWN = ("right", 1)
LEFT_UP = ("left", 0)
LEFT_DOWN = ("left", 1)
TOP_RIGHT = ("top", 0)
TOP_LEFT = ("top", 1)
BOTTOM_RIGHT = ("bottom", 0)
BOTTOM_LEFT = ("bottom", 1)
FRONT_RIGHT = ("front", 0)
FRONT_LEFT = ("front", 1)
BACK_RIGHT = ("back", 0)
BACK_LEFT = ("back", 1)

moves_made = []
def clear_moves():
    moves_made.clear()
def make_move(f, d, c):
    moves_made.append((f, d))
    return [c[i] for i in MOVES[f][d]]

def make_moves(move_lst, c):
    for f, d in move_lst:
        c = make_move(f, d, c)
    return c

def make_moves_rev(move_list, c):
    return make_moves([(m[0], (m[1]+1)%2) for m in move_list[::-1]], c)

def all_moves(c):
    for f in MOVES:
        yield make_move(f, 0, c), (f, 0)
        yield make_move(f, 1, c), (f, 1)

def random_move(c):
    f, d = random.sample(MOVES.keys(), 1)[0], random.randint(0, 1)
    return make_move(f, d, c), (f, d)

def scramble(c, n=100):
    moves = []
    for i in range(n):
        c, move = random_move(c)
        moves.append(move)
    return c, moves

def find_piece(c, p):
    return c.index(p)

SOLVED = list(range(54))

def match(mask, c):
    for m, p, s in zip(mask, c, SOLVED):
        if not (m == '*' or (m == 'c' and p//9 == s//9) or p == s):
            if m == 'c':
                print("expected", colors[s//9], "but was", colors[p//9], "at s="+str(s))
            else:
                print("expecting %s but got %s" % (s, p))
            return False
    return True

def test():
    for move in MOVES:
        if make_move(move, 1, make_move(move, 0, SOLVED)) != SOLVED:
            print('error in move and back', move)
        if make_moves([(move, 0)]*4, SOLVED) != SOLVED:
            print('error in move around forward', move)
        if make_moves([(move, 1)]*4, SOLVED) != SOLVED:
            print('error in move around backward', move)
        if len(set(MOVES[move][0])) != 54:
            print('error in', move, 0)
        if len(set(MOVES[move][1])) != 54:
            print('error in', move, 1)
    for shift in SHIFTS:
        if make_shift(shift, 1, make_shift(shift, 0, SOLVED)) != SOLVED:
            print('error in shift', shift)
        if make_shifts([(shift, 0)]*4, SOLVED) != SOLVED:
            print('error in shift around forward', shift)
        if make_shifts([(shift, 1)]*4, SOLVED) != SOLVED:
            print('error in shift around backward', shift)
        if len(set(SHIFTS[shift][0])) != 54:
            print('error in', shift, 0)
        if len(set(SHIFTS[shift][1])) != 54:
            print('error in', shift, 1)
    for i in range(100):
        c, moves = scramble(SOLVED)
        if make_moves_rev(moves, c) != SOLVED:
            print('error in scramble/reverse')
            break

def main():
    test()

if __name__ == '__main__':
    main()
