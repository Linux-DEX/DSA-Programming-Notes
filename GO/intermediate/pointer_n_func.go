package main

import "fmt"

// taking a function with integer type pointer as an parameter
func ptf(a *int) {
	// dereferencing
	*a = 748
}

func main() {
	// taking a normal variable
	var x = 100

	fmt.Printf("The value of x before function call is: %d\n", x)

	// taking a pointer variable and assigning the address of x to it
	var pa *int = &x

	// calling the function by passing pointer to function
	ptf(pa)

	// calling the function by passing the address of the variable x
    ptf(&x)

	fmt.Printf("The value of x after function call is: %d\n", x)
}
