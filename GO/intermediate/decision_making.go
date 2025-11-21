package main

import "fmt"

func main() {
	var v int = 1217
	var v1 int = 400
	var v2 int = 700

	// if statement
	if v < 1000 {
		fmt.Printf("v is less than 1000\n")
	}
	fmt.Printf("value of v is : %d\n", v)

	// if else statement
	if v < 1000 {
		fmt.Printf("v is less than 1000\n")
	} else {
		fmt.Printf("v is greather than 1000\n")
	}

	// nested if statement
	if v1 == 400 {
		if v2 == 700 {
			fmt.Printf("Value of v1 is 400 and v2 is 700\n")
		}
	}

	// if_else_if ladder
	if v1 == 100 {
		fmt.Printf("Value of v1 is 100\n")
	} else if v1 == 200 {
		fmt.Printf("Value of a is 20\n")
	} else if v1 == 300 {
		fmt.Printf("Value of a is 300\n")
	} else {
		fmt.Printf("None of the values is matching\n")
	}
}
