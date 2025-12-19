package main

import (
	"fmt"
)

func main() {
	// storing the hexadecimal values in variables
	x := 0xFF
	y := 0x9C

	// Displaying the values
	fmt.Printf("Type of variable x is %T\n", x)
	fmt.Printf("Value of x in hexadecimal is %X\n", x)
	fmt.Printf("Value of x in decimal is %v\n", x)

	fmt.Printf("Type of variable y is %T\n", y)
	fmt.Printf("Value of y in hexadecimal is %X\n", y)
	fmt.Printf("Value of y in decimal is %v\n", y)

	// taking a normal variable
	var val int = 5748

	// declaration of pointer
	var p *int

	// displaying the result
	fmt.Println("p = ", p)

	// initialization of pointer
	p = &val

	fmt.Println("Value stored in val = ", val)
	fmt.Println("Address of val = ", &val)
	fmt.Println("Value stored in variable p = ", p)

	// using var keyword we are not defining any type with variable
	var z = 458

	// taking a pointer variable using var keyword without specifying the type
	var ptr = &z

	fmt.Println("Value stored in z before changing = ", z)
	fmt.Println("Address of z = ", &z)
	fmt.Println("Value stored in pointer variable ptr = ", ptr)

	// this is dereferencing a pointer using * operator before a pointer variable to access the value stored at the variable at which it is pointing
	fmt.Println("Value stored in z(*ptr) Before Changing = ", *ptr)

	// changing the value of z by assigning the new value to the pointer
	*ptr = 500

	fmt.Println("Value stored in z(*ptr) after Changing = ", z)
}
