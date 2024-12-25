package sliceutil

import "fmt"

func Map[T, U any](slice []T, f func(T) U) []U {
	result := make([]U, len(slice))

	for i, v := range slice {
		result[i] = f(v)
	}

	return result
}

func DebugPrint[T any](slice []T) {
	fmt.Print("[")
	for i, v := range slice {
		fmt.Printf("%v", v)
		if i != len(slice)-1 {
			fmt.Print(", ")
		}
	}
	fmt.Print("]\n")
}
