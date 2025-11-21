/*
declaring a variables
var <variable_name> <type> = <expression>
*/

package main

import (
	"fmt"
)

func main() {
	// initialized without the explicit type
	var myvar1 = 20
	var myvar2 = "Linux-DEX"
	var myvar3 = 34.80

	fmt.Printf("\nThe value of myvar1 is : %d\n", myvar1)
	fmt.Printf("The type of myvar1 is : %T\n", myvar1)
	fmt.Printf("The value of myvar2 is : %s\n", myvar2)
	fmt.Printf("The type of myvar2 is : %T\n", myvar2)
	fmt.Printf("The value of myvar3 is : %f\n", myvar3)
	fmt.Printf("The type of myvar3 is : %T\n", myvar3)

	// initialized without expression
	var myvariable1 int
	var myvariable2 string
	var myvariable3 float64

	fmt.Printf("\nThe value of myvariable1 is : %d\n", myvariable1)
	fmt.Printf("The value of myvariable2 is : %s\n", myvariable2)
	fmt.Printf("The value of myvariable3 is : %f\n", myvariable3)

	// multiple vairable of the same type are declared and initialized in the single line
	var var1, var2, var3 int = 32, 456, 74

	fmt.Printf("\nThe value of var1 is : %d\n", var1)
	fmt.Printf("The value of var2 is : %d\n", var2)
	fmt.Printf("The value of var3 is : %d\n", var3)

	// Multiple variables of different types are declared and initialized in the single line
	var variable1, variable2, variable3 = 2, "GFG", 67.56

	fmt.Printf("\nThe value of variable1 is : %d\n", variable1)
	fmt.Printf("The type of variable1 is : %T\n", variable1)
	fmt.Printf("The value of variable2 is : %s\n", variable2)
	fmt.Printf("The type of variable2 is : %T\n", variable2)
	fmt.Printf("The value of variable3 is : %f\n", variable3)
	fmt.Printf("The type of variable3 is : %T\n", variable3)

	// Using short variable declaration
	svar1 := 39
	svar2 := "Linuxdex"
	svar3 := 34.98

	fmt.Printf("\nThe value of svar1 is : %d\n", svar1)
	fmt.Printf("The type of svar1 is : %T\n", svar1)
	fmt.Printf("The value of svar2 is : %s\n", svar2)
	fmt.Printf("The type of svar2 is : %T\n", svar2)
	fmt.Printf("The value of svar3 is : %f\n", svar3)
	fmt.Printf("The type of svar3 is : %T\n", svar3)

	// Using short variable declaration Multiple variables of same types are declared and initialized in the single line
	msvar1, msvar2, msvar3 := 800, 34, 56

	fmt.Printf("\nThe value of msvar1 is : %d\n", msvar1)
	fmt.Printf("The type of msvar1 is : %T\n", msvar1)
	fmt.Printf("The value of msvar2 is : %d\n", msvar2)
	fmt.Printf("The type of msvar2 is : %T\n", msvar2)
	fmt.Printf("The value of msvar3 is : %d\n", msvar3)
	fmt.Printf("The type of msvar3 is : %T\n", msvar3)

	// Using short variable declaration Multiple variables of different types are declared and initialized in the single line
	svariable1, svariable2, svariable3 := 800, "Geeks", 47.56

	fmt.Printf("\nThe value of svariable1 is : %d\n", svariable1)
	fmt.Printf("The type of svariable1 is : %T\n", svariable1)
	fmt.Printf("The value of svariable2 is : %s\n", svariable2)
	fmt.Printf("The type of svariable2 is : %T\n", svariable2)
	fmt.Printf("The value of svariable3 is : %f\n", svariable3)
	fmt.Printf("The type of svariable3 is : %T\n", svariable3)
}
