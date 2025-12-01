package main

import (
	"fmt"
)

func main() {
	// calling the function
	// function returns two values which are
	// assigned to mul and blank identifier
	mul, _ := mul_div(105, 7)

	fmt.Println("105 x 7 = ", mul)

	sum := 0
	for _, value := range []int{1, 2, 3} { // Index is ignored with _
		sum += value
	}

}

// function returning two values of integer type
func mul_div(n1 int, n2 int) (int, int) {

	return n1 * n2, n1 / n2
}
