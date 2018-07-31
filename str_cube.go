package main

import (
	"fmt"
	"math/rand"
	//"strings"
)

type Move struct {
	f string
	d int
}

func (m Move) rev() Move {
	return Move{m.f, (m.d + 1) % 2}
}

const (
	TOP    = 0
	FRONT  = 1
	RIGHT  = 2
	BOTTOM = 3
	BACK   = 4
	LEFT   = 5
)

var (
	colors = []string{"w", "o", "g", "y", "r", "b"}
	//SOLVED = []int{36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 0, 1, 2, 18, 19, 20, 48, 49, 50, 3, 4, 5, 21, 22, 23, 51, 52, 53, 6, 7, 8, 24, 25, 26, 9, 10, 11, 12, 13, 14, 15, 16, 17, 27, 28, 29, 30, 31, 32, 33, 34, 35}
	SOLVED = []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53}
	SHIFTS = map[string][][]int{
		"vert": [][]int{[]int{
			9, 10, 11, 12, 13, 14, 15, 16, 17,
			27, 28, 29, 30, 31, 32, 33, 34, 35,
			24, 21, 18, 25, 22, 19, 26, 23, 20,
			36, 37, 38, 39, 40, 41, 42, 43, 44,
			0, 1, 2, 3, 4, 5, 6, 7, 8,
			47, 50, 53, 46, 49, 52, 45, 48, 51}, []int{
			36, 37, 38, 39, 40, 41, 42, 43, 44,
			0, 1, 2, 3, 4, 5, 6, 7, 8,
			20, 23, 26, 19, 22, 25, 18, 21, 24,
			9, 10, 11, 12, 13, 14, 15, 16, 17,
			27, 28, 29, 30, 31, 32, 33, 34, 35,
			51, 48, 45, 52, 49, 46, 53, 50, 47}},
		"side": [][]int{[]int{
			2, 5, 8, 1, 4, 7, 0, 3, 6,
			47, 50, 53, 46, 49, 52, 45, 48, 51,
			11, 14, 17, 10, 13, 16, 9, 12, 15,
			33, 30, 27, 34, 31, 28, 35, 32, 29,
			20, 23, 26, 19, 22, 25, 18, 21, 24,
			38, 41, 44, 37, 40, 43, 36, 39, 42}, []int{
			6, 3, 0, 7, 4, 1, 8, 5, 2,
			24, 21, 18, 25, 22, 19, 26, 23, 20,
			42, 39, 36, 43, 40, 37, 44, 41, 38,
			29, 32, 35, 28, 31, 34, 27, 30, 33,
			51, 48, 45, 52, 49, 46, 53, 50, 47,
			15, 12, 9, 16, 13, 10, 17, 14, 11}}}
	MOVES = map[string][][]int{
		"right": [][]int{[]int{
			0, 1, 11, 3, 4, 14, 6, 7, 17,
			9, 10, 29, 12, 13, 32, 15, 16, 35,
			24, 21, 18, 25, 22, 19, 26, 23, 20,
			27, 28, 38, 30, 31, 41, 33, 34, 44,
			36, 37, 2, 39, 40, 5, 42, 43, 8,
			45, 46, 47, 48, 49, 50, 51, 52, 53}, []int{
			0, 1, 38, 3, 4, 41, 6, 7, 44,
			9, 10, 2, 12, 13, 5, 15, 16, 8,
			20, 23, 26, 19, 22, 25, 18, 21, 24,
			27, 28, 11, 30, 31, 14, 33, 34, 17,
			36, 37, 29, 39, 40, 32, 42, 43, 35,
			45, 46, 47, 48, 49, 50, 51, 52, 53}},
		"left": [][]int{[]int{
			9, 1, 2, 12, 4, 5, 15, 7, 8,
			27, 10, 11, 30, 13, 14, 33, 16, 17,
			18, 19, 20, 21, 22, 23, 24, 25, 26,
			36, 28, 29, 39, 31, 32, 42, 34, 35,
			0, 37, 38, 3, 40, 41, 6, 43, 44,
			47, 50, 53, 46, 49, 52, 45, 48, 51}, []int{
			36, 1, 2, 39, 4, 5, 42, 7, 8,
			0, 10, 11, 3, 13, 14, 6, 16, 17,
			18, 19, 20, 21, 22, 23, 24, 25, 26,
			9, 28, 29, 12, 31, 32, 15, 34, 35,
			27, 37, 38, 30, 40, 41, 33, 43, 44,
			51, 48, 45, 52, 49, 46, 53, 50, 47}},
		"top": [][]int{[]int{
			2, 5, 8, 1, 4, 7, 0, 3, 6,
			47, 50, 53, 12, 13, 14, 15, 16, 17,
			11, 19, 20, 10, 22, 23, 9, 25, 26,
			27, 28, 29, 30, 31, 32, 33, 34, 35,
			36, 37, 38, 39, 40, 41, 18, 21, 24,
			45, 46, 44, 48, 49, 43, 51, 52, 42}, []int{
			6, 3, 0, 7, 4, 1, 8, 5, 2,
			24, 21, 18, 12, 13, 14, 15, 16, 17,
			42, 19, 20, 43, 22, 23, 44, 25, 26,
			27, 28, 29, 30, 31, 32, 33, 34, 35,
			36, 37, 38, 39, 40, 41, 53, 50, 47,
			45, 46, 9, 48, 49, 10, 51, 52, 11}},
		"bottom": [][]int{[]int{
			0, 1, 2, 3, 4, 5, 6, 7, 8,
			9, 10, 11, 12, 13, 14, 45, 48, 51,
			18, 19, 17, 21, 22, 16, 24, 25, 15,
			33, 30, 27, 34, 31, 28, 35, 32, 29,
			20, 23, 26, 39, 40, 41, 42, 43, 44,
			38, 46, 47, 37, 49, 50, 36, 52, 53}, []int{
			0, 1, 2, 3, 4, 5, 6, 7, 8,
			9, 10, 11, 12, 13, 14, 26, 23, 20,
			18, 19, 36, 21, 22, 37, 24, 25, 38,
			29, 32, 35, 28, 31, 34, 27, 30, 33,
			51, 48, 45, 39, 40, 41, 42, 43, 44,
			15, 46, 47, 16, 49, 50, 17, 52, 53}},
		"front": [][]int{[]int{
			0, 1, 2, 3, 4, 5, 51, 52, 53,
			15, 12, 9, 16, 13, 10, 17, 14, 11,
			18, 19, 20, 21, 22, 23, 6, 7, 8,
			26, 25, 24, 30, 31, 32, 33, 34, 35,
			36, 37, 38, 39, 40, 41, 42, 43, 44,
			45, 46, 47, 48, 49, 50, 29, 28, 27}, []int{
			0, 1, 2, 3, 4, 5, 24, 25, 26,
			11, 14, 17, 10, 13, 16, 9, 12, 15,
			18, 19, 20, 21, 22, 23, 29, 28, 27,
			53, 52, 51, 30, 31, 32, 33, 34, 35,
			36, 37, 38, 39, 40, 41, 42, 43, 44,
			45, 46, 47, 48, 49, 50, 6, 7, 8}},
		"back": [][]int{[]int{
			45, 46, 47, 3, 4, 5, 6, 7, 8,
			9, 10, 11, 12, 13, 14, 15, 16, 17,
			0, 1, 2, 21, 22, 23, 24, 25, 26,
			27, 28, 29, 30, 31, 32, 20, 19, 18,
			38, 41, 44, 37, 40, 43, 36, 39, 42,
			35, 34, 33, 48, 49, 50, 51, 52, 53}, []int{
			18, 19, 20, 3, 4, 5, 6, 7, 8,
			9, 10, 11, 12, 13, 14, 15, 16, 17,
			35, 34, 33, 21, 22, 23, 24, 25, 26,
			27, 28, 29, 30, 31, 32, 47, 46, 45,
			42, 39, 36, 43, 40, 37, 44, 41, 38,
			0, 1, 2, 48, 49, 50, 51, 52, 53}}}
)

func make_shift(m Move, c []int) []int {
	rc := make([]int, len(c))
	for i := 0; i < len(c); i++ {
		rc[i] = c[SHIFTS[m.f][m.d][i]]
	}
	return rc
}

func make_shifts(m []Move, c []int) []int {
	for i := 0; i < len(m); i++ {
		c = make_shift(m[i], c)
	}
	return c
}

func make_shifts_rev(m []Move, c []int) []int {
	for i := len(m) - 1; i > -1; i-- {
		c = make_shift(m[i].rev(), c)
	}
	return c
}

func all_shifts(c []int) [][]int {
	res := make([][]int, len(SHIFTS)*2)
	for f := range SHIFTS {
		res = append(res, make_shift(Move{f, 0}, c))
		res = append(res, make_shift(Move{f, 1}, c))
	}
	return res
}

func random_shift(c []int) ([]int, Move) {
	var m Move
	i := 0
	tf := rand.Intn(len(SHIFTS))
	for face := range SHIFTS {
		if i == tf {
			m.f = face
			break
		}
		i++
	}
	m.d = rand.Intn(2)
	return make_shift(m, c), m
}

func make_move(m Move, c []int) []int {
	//fmt.Println(display_i(c))
	rc := make([]int, len(c))
	for i := 0; i < len(c); i++ {
		rc[i] = c[MOVES[m.f][m.d][i]]
	}
	return rc
}

func make_moves(m []Move, c []int) []int {
	for i := 0; i < len(m); i++ {
		c = make_move(m[i], c)
	}
	return c
}

func make_moves_rev(m []Move, c []int) []int {
	for i := len(m) - 1; i > -1; i-- {
		c = make_move(m[i].rev(), c)
	}
	return c
}

func all_moves(c []int) [][]int {
	res := make([][]int, len(MOVES)*2)
	for f := range MOVES {
		// should be assign instead of append?
		res = append(res, make_move(Move{f, 0}, c))
		res = append(res, make_move(Move{f, 1}, c))
	}
	return res
}

func random_move(c []int) ([]int, Move) {
	var m Move
	i := 0
	tf := rand.Intn(len(MOVES))
	for face := range MOVES {
		if i == tf {
			m.f = face
			break
		}
		i++
	}
	m.d = rand.Intn(2)
	return make_move(m, c), m
}

func scramble(c []int, n int) ([]int, []Move) {
	moves := make([]Move, n)
	var m Move
	for i := 0; i < n; i++ {
		c, m = random_move(c)
		moves[i] = m
	}
	return c, moves
}

func color_cube(c []int) []string {
	c_str := make([]string, len(c))
	for i, v := range c {
		c_str[i] = colors[v/9]
	}
	return c_str
}

func display_s(c []string) string {
	return fmt.Sprintf("          %2s %2s %2s\n          %2s %2s %2s\n          %2s %2s %2s\n\n%2s %2s %2s  %2s %2s %2s  %2s %2s %2s\n%2s %2s %2s  %2s %2s %2s  %2s %2s %2s\n%2s %2s %2s  %2s %2s %2s  %2s %2s %2s\n\n          %2s %2s %2s\n          %2s %2s %2s\n          %2s %2s %2s\n\n          %2s %2s %2s\n          %2s %2s %2s\n          %2s %2s %2s", c[36], c[37], c[38], c[39], c[40], c[41], c[42], c[43], c[44], c[45], c[46], c[47], c[0], c[1], c[2], c[18], c[19], c[20], c[48], c[49], c[50], c[3], c[4], c[5], c[21], c[22], c[23], c[51], c[52], c[53], c[6], c[7], c[8], c[24], c[25], c[26], c[9], c[10], c[11], c[12], c[13], c[14], c[15], c[16], c[17], c[27], c[28], c[29], c[30], c[31], c[32], c[33], c[34], c[35])
}
func display_i(c []int) string {
	return fmt.Sprintf("          %2d %2d %2d\n          %2d %2d %2d\n          %2d %2d %2d\n\n%2d %2d %2d  %2d %2d %2d  %2d %2d %2d\n%2d %2d %2d  %2d %2d %2d  %2d %2d %2d\n%2d %2d %2d  %2d %2d %2d  %2d %2d %2d\n\n          %2d %2d %2d\n          %2d %2d %2d\n          %2d %2d %2d\n\n          %2d %2d %2d\n          %2d %2d %2d\n          %2d %2d %2d", c[36], c[37], c[38], c[39], c[40], c[41], c[42], c[43], c[44], c[45], c[46], c[47], c[0], c[1], c[2], c[18], c[19], c[20], c[48], c[49], c[50], c[3], c[4], c[5], c[21], c[22], c[23], c[51], c[52], c[53], c[6], c[7], c[8], c[24], c[25], c[26], c[9], c[10], c[11], c[12], c[13], c[14], c[15], c[16], c[17], c[27], c[28], c[29], c[30], c[31], c[32], c[33], c[34], c[35])
}
func display_c(c []int) string {
	return display_s(color_cube(c))
}

func comp_int_arr(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func test() {
	for f := range MOVES {
		if !comp_int_arr(make_move(Move{f, 1}, make_move(Move{f, 0}, SOLVED)), SOLVED) {
			fmt.Println("error in move and back", f)
		}
		if !comp_int_arr(
			make_moves([]Move{Move{f, 0}, Move{f, 0}, Move{f, 0}, Move{f, 0}}, SOLVED),
			SOLVED) {
			fmt.Println("error in move around forward", f)
		}
		if !comp_int_arr(
			make_moves([]Move{Move{f, 1}, Move{f, 1}, Move{f, 1}, Move{f, 1}}, SOLVED),
			SOLVED) {
			fmt.Println("error in move around backward", f)
		}
	}
	for f := range SHIFTS {
		if !comp_int_arr(make_shift(Move{f, 1}, make_shift(Move{f, 0}, SOLVED)), SOLVED) {
			fmt.Println("error in shift and back", f)
		}
		if !comp_int_arr(
			make_shifts([]Move{Move{f, 0}, Move{f, 0}, Move{f, 0}, Move{f, 0}}, SOLVED),
			SOLVED) {
			fmt.Println("error in shift around forward", f)
		}
		if !comp_int_arr(
			make_shifts([]Move{Move{f, 1}, Move{f, 1}, Move{f, 1}, Move{f, 1}}, SOLVED),
			SOLVED) {
			fmt.Println("error in shift around backward", f)
		}
	}
	for si := 0; si < 100; si++ {
		c, moves := scramble(SOLVED, 100)
		if !comp_int_arr(make_moves_rev(moves, c), SOLVED) {
			fmt.Println("error in scramble/reverse")
		}
	}
}

func main() {
	test()
}
