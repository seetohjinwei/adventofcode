package main

import (
	"fmt"
	"os"
	"strings"

	"github.com/seetohjinwei/adventofcode/year2024/utils/errorutil"
)

func getInput() [][]rune {
	b, err := os.ReadFile("day04/day04.in")
	errorutil.AssertNil(err)

	space := make([][]rune, 0)

	for _, s := range strings.Split(string(b), "\n") {
		row := make([]rune, 0, len(s))

		for _, c := range s {
			row = append(row, c)
		}

		space = append(space, row)
	}

	return space
}

var XMAS = []rune{'X', 'M', 'A', 'S'}

type Coord struct {
	r int
	c int
}

func (d Coord) add(other Coord) Coord {
	return Coord{
		r: d.r + other.r,
		c: d.c + other.c,
	}
}

func (d Coord) isValid(m, n int) bool {
	return d.r >= 0 && d.c >= 0 && d.r < m && d.c < n
}

func (d Coord) get(space [][]rune) rune {
	return space[d.r][d.c]
}

// Returns nil if invalid
func (d Coord) getBox(space [][]rune) [][]rune {
	m := len(space)
	n := len(space[0])

	if d.r-1 < 0 || d.r+1 >= m || d.c-1 < 0 || d.c+1 >= n {
		return nil
	}

	box := make([][]rune, 0, 3)

	for _, row := range space[d.r-1 : d.r+2] {
		box = append(box, row[d.c-1:d.c+2])
	}

	return box
}

var (
	left   = Coord{0, -1}
	right  = Coord{0, 1}
	top    = Coord{-1, 0}
	bottom = Coord{1, 0}

	bottomRight = Coord{1, 1}
	bottomLeft  = Coord{-1, 1}
	topRight    = Coord{1, -1}
	topLeft     = Coord{-1, -1}

	dirs = []Coord{left, right, top, bottom, bottomRight, bottomLeft, topRight, topLeft}
)

// r, c represents coordinates for X
func getXMAS(space [][]rune, m, n, r, c int) int {
	count := 0

	start := Coord{r, c}

	for _, dir := range dirs {
		isSuccess := true

		curr := start
		for _, expected := range XMAS {
			if !curr.isValid(m, n) {
				isSuccess = false
				break
			}
			if curr.get(space) != expected {
				isSuccess = false
				break
			}
			curr = curr.add(dir)
		}

		if isSuccess {
			count++
		}
	}

	return count
}

func part1(space [][]rune) int {
	count := 0

	m := len(space)
	n := len(space[0])

	for r, row := range space {
		for c, char := range row {
			if char != 'X' {
				continue
			}
			count += getXMAS(space, m, n, r, c)
		}
	}

	return count
}

// r, c represents coordinates for the A in the centre
func getX_MAS(space [][]rune, r, c int) int {
	start := Coord{r, c}

	box := start.getBox(space)
	if box == nil {
		return 0
	}

	x1 := box[0][0]
	x2 := box[0][2]
	x3 := box[2][0]
	x4 := box[2][2]

	if x1 == 'M' && x2 == 'M' && x3 == 'S' && x4 == 'S' {
		return 1
	} else if x1 == 'M' && x2 == 'S' && x3 == 'M' && x4 == 'S' {
		return 1
	} else if x1 == 'S' && x2 == 'M' && x3 == 'S' && x4 == 'M' {
		return 1
	} else if x1 == 'S' && x2 == 'S' && x3 == 'M' && x4 == 'M' {
		return 1
	}

	return 0
}

func part2(space [][]rune) int {
	count := 0

	for r, row := range space {
		for c, char := range row {
			if char != 'A' {
				continue
			}
			count += getX_MAS(space, r, c)
		}
	}

	return count
}

func main() {
	space := getInput()

	result1 := part1(space)
	fmt.Printf("Part 1: %d\n", result1)

	result2 := part2(space)
	fmt.Printf("Part 2: %d\n", result2)
}
