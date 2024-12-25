package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"

	"github.com/seetohjinwei/adventofcode/year2024/utils/errorutil"
)

type Token rune

const (
	TokenM Token = iota
	TokenU
	TokenL
	TokenParenOpen
	TokenDigit
	TokenComma
	TokenParenClose

	TokenD
	TokenO
	TokenN
	TokenApos
	TokenT

	TokenUnknown
)

func getTokenType(char rune) Token {
	if char == 'm' {
		return TokenM
	} else if char == 'u' {
		return TokenU
	} else if char == 'l' {
		return TokenL
	} else if char == '(' {
		return TokenParenOpen
	} else if '0' <= char && char <= '9' {
		return TokenDigit
	} else if char == ',' {
		return TokenComma
	} else if char == ')' {
		return TokenParenClose
	} else if char == 'd' {
		return TokenD
	} else if char == 'o' {
		return TokenO
	} else if char == 'n' {
		return TokenN
	} else if char == '\'' {
		return TokenApos
	} else if char == 't' {
		return TokenT
	}

	return TokenUnknown
}

func getInstructions() string {
	b, err := os.ReadFile("day03/day03.in")
	errorutil.AssertNil(err)

	return string(b)
}

func part1(instructions string) int {
	sum := 0

	nextTokens := []Token{TokenM}

	firstNum := 0
	currNum := 0

	for _, char := range instructions {
		token := getTokenType(char)
		if !slices.Contains(nextTokens, token) {
			// reset parser
			nextTokens = []Token{TokenM}
			firstNum = 0
			currNum = 0
			continue
		}

		if token == TokenM {
			nextTokens = []Token{TokenU}
		} else if token == TokenU {
			nextTokens = []Token{TokenL}
		} else if token == TokenL {
			nextTokens = []Token{TokenParenOpen}
		} else if token == TokenParenOpen {
			nextTokens = []Token{TokenDigit}
		} else if token == TokenDigit {
			digit, err := strconv.Atoi(string(char))
			errorutil.AssertNil(err)
			currNum = currNum*10 + digit
			nextTokens = []Token{TokenDigit, TokenComma, TokenParenClose}
		} else if token == TokenComma {
			firstNum = currNum
			currNum = 0
			nextTokens = []Token{TokenDigit}
		} else if token == TokenParenClose {
			sum += firstNum * currNum
			nextTokens = []Token{TokenM}
			firstNum = 0
			currNum = 0
		}
	}

	return sum
}

func part2(instructions string) int {
	sum := 0

	enableMul := true
	nextTokens := []Token{TokenM}
	prevToken := TokenUnknown

	firstNum := 0
	currNum := 0

	for i, char := range instructions {
		token := getTokenType(char)
		if !slices.Contains(nextTokens, token) {
			// reset parser
			nextTokens = []Token{TokenM, TokenD}
			firstNum = 0
			currNum = 0
			continue
		}

		if token == TokenM {
			nextTokens = []Token{TokenU}
		} else if token == TokenU {
			nextTokens = []Token{TokenL}
		} else if token == TokenL {
			nextTokens = []Token{TokenParenOpen}
		} else if token == TokenParenOpen {
			if prevToken == TokenO || prevToken == TokenT {
				nextTokens = []Token{TokenParenClose}
			} else {
				nextTokens = []Token{TokenDigit}
			}
		} else if token == TokenDigit {
			digit, err := strconv.Atoi(string(char))
			errorutil.AssertNil(err)
			currNum = currNum*10 + digit
			nextTokens = []Token{TokenDigit, TokenComma, TokenParenClose}
		} else if token == TokenComma {
			firstNum = currNum
			currNum = 0
			nextTokens = []Token{TokenDigit}
		} else if token == TokenParenClose {
			prevPrevToken := getTokenType(rune(instructions[i-2]))
			if prevPrevToken == TokenO {
				// do()
				enableMul = true
			} else if prevPrevToken == TokenT {
				// don't()
				enableMul = false
			} else if enableMul {
				sum += firstNum * currNum
			}

			nextTokens = []Token{TokenM, TokenD}
			firstNum = 0
			currNum = 0
		} else if token == TokenD {
			nextTokens = []Token{TokenO}
		} else if token == TokenO {
			nextTokens = []Token{TokenN, TokenParenOpen}
		} else if token == TokenN {
			nextTokens = []Token{TokenApos}
		} else if token == TokenApos {
			nextTokens = []Token{TokenT}
		} else if token == TokenT {
			nextTokens = []Token{TokenParenOpen}
		}

		prevToken = token
	}

	return sum
}

func main() {
	instructions := getInstructions()

	result1 := part1(instructions)
	fmt.Printf("Part 1: %d\n", result1)

	result2 := part2(instructions)
	fmt.Printf("Part 2: %d\n", result2)
}
