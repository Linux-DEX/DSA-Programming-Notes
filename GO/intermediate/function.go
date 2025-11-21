package main

import (
	"fmt"
)

// function declaration
func multiply(a, b int) int {
	return a * b
}

func multiply_fn(a, b *int) int {
	*a = *a * 2 // modifying a's value at its memory address.
	return *a * *b
}

func main() {
	// function calling
	// call by value
	mul_res := multiply(5, 82)
	fmt.Printf("multiplication: %d\n", mul_res)

	// call by reference
	x := 5
	y := 10
	res := multiply_fn(&x, &y)
	fmt.Printf("call by reference, multiplication: %d\n", res)
}
