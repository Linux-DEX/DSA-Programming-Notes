// Declares that this file is part of the main package, indicating an executable program
package main

// Imports the "fmt" package, which provides functions for formatted I/O, like printing to the console
import "fmt"

// func main() { // main function
// 	fmt.Println("Hello world!")  // print hello world!
// }

func main() {
	var num1, num2 int

	fmt.Println("enter first number")
	fmt.Scan(&num1)
	fmt.Println("enter second number")
	fmt.Scan(&num2)

	sum := num1 + num2

	fmt.Println("The Sum is : ", sum)
}