package main

import "fmt"

// Passing anonymous function as an argument
func DEX(i func(p, q string) string) {
	fmt.Println(i("Linux", "-"))
}

// Returning anonymous function
func golang() func(i, j string) string {
	myf := func(i, j string) string {
		return i + j + "GO Programming Language"
	}
	return myf
}

func main() {
	// simple Anonymous function
	func() {
		fmt.Println("Welcome! to GO Programming")
	}()

	// Assigning an anonymous function to a variable
	value := func() {
		fmt.Println("Welcome! to GO language")
	}
	value()

	// Passing arguments in anonymous function
	func(ele string) {
		fmt.Println(ele)
	}("Linux DEX")

	// passing anonymous func
	values := func(p, q string) string {
		return p + q + "DEX"
	}
	DEX(values)

	// Returning Anonymous func
	res_value := golang()
	fmt.Println(res_value("Welcome ", "to "))
}
