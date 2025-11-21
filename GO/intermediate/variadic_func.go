package main

import "fmt"

// Variadic function to calculate sum
func sum(nums ...int) int {
	total := 0
	for _, n := range nums {
		total += n
	}
	return total
}

// Variadic func with other parameter
func greet(prefix string, nums ...int) {
	fmt.Println(prefix)
	for _, n := range nums {
		fmt.Println("Number:", n)
	}
}

func main() {
	fmt.Println("Sum of 1, 2, 3:", sum(1, 2, 3))
	fmt.Println("Sum of 4, 5:", sum(4, 5))
	fmt.Println("Sum of no numbers:", sum())

	greet("Sum of numbers:", 1, 2, 3)
	greet("Another sum:", 4, 5)
	greet("No numbers sum:")
}
