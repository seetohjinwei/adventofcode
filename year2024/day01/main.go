package main

import (
	"bytes"
	"fmt"
	"os"
	"slices"
	"strconv"

	"github.com/seetohjinwei/adventofcode/year2024/utils/errorutil"
	"github.com/seetohjinwei/adventofcode/year2024/utils/stringutil"
)

func getInput() ([]int, []int) {
	b, err := os.ReadFile("day01/part1.in")
	errorutil.AssertNil(err)

	var left, right []int

	rows := bytes.Split(b, []byte("\n"))

	for _, row := range rows {
		parts := stringutil.SplitWhitespace(string(row))
		errorutil.Assert(len(parts) == 2, "should have 2 parts")

		x, err := strconv.Atoi(parts[0])
		errorutil.AssertNil(err)
		y, err := strconv.Atoi(parts[1])
		errorutil.AssertNil(err)

		left = append(left, x)
		right = append(right, y)
	}

	errorutil.Assert(len(left) == len(right))

	slices.Sort(left)
	slices.Sort(right)

	return left, right
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func part1(left, right []int) int {
	diff := 0

	for i := 0; i < len(left); i++ {
		diff += abs(left[i] - right[i])
	}

	return diff
}

func part2(left, right []int) int {
	counter := make(map[int]int)
	for _, v := range right {
		counter[v]++
	}

	score := 0

	for _, v := range left {
		score += v * counter[v]
	}

	return score
}

func main() {
	left, right := getInput()

	result1 := part1(left, right)
	fmt.Printf("Part 1: %d\n", result1)

	result2 := part2(left, right)
	fmt.Printf("Part 2: %d\n", result2)
}
