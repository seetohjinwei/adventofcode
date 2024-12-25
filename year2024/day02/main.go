package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"

	"github.com/seetohjinwei/adventofcode/year2024/utils/errorutil"
	"github.com/seetohjinwei/adventofcode/year2024/utils/numberutil"
	"github.com/seetohjinwei/adventofcode/year2024/utils/sliceutil"
)

func getReports() [][]int {
	b, err := os.ReadFile("day02/part1.in")
	errorutil.AssertNil(err)

	reports := make([][]int, 0)

	rows := strings.Split(string(b), "\n")
	for _, row := range rows {
		reportString := strings.Split(row, " ")
		report := sliceutil.Map(reportString, func(v string) int {
			x, err := strconv.Atoi(v)
			errorutil.AssertNil(err)
			return x
		})

		reports = append(reports, report)
	}

	return reports
}

func isSafe(report []int) bool {
	isIncreasing := report[0] < report[1]
	prev := report[0]

	for i := 1; i < len(report); i++ {
		curr := report[i]

		if (prev < curr) != isIncreasing {
			return false
		}

		diff := numberutil.AbsInt(prev - curr)
		if diff < 1 || diff > 3 {
			return false
		}

		prev = curr
	}

	return true
}

func part1(reports [][]int) int {
	count := 0

	for _, report := range reports {
		if isSafe(report) {
			count++
		}
	}

	return count
}

func isPart2Safe(report []int) bool {
	for i := range report {
		r := slices.Clone(report)
		r = slices.Delete(r, i, i+1)
		if isSafe(r) {
			return true
		}
	}

	return false
}

func part2(reports [][]int) int {
	count := 0

	for _, report := range reports {
		if isPart2Safe(report) {
			count++
		}
	}

	return count
}

func main() {
	reports := getReports()

	result1 := part1(reports)
	fmt.Printf("Part 1: %d\n", result1)

	result2 := part2(reports)
	fmt.Printf("Part 2: %d\n", result2)
}
