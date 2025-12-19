package main

import "fmt"

// Defining a struct
type Person struct {
	name string
	age  int
}

func main() {
	// Creating an instance of the struct
	p1 := Person{name: "A", age: 25}

	// Creating a pointer to the struct
	personPointer := &p1

	// Accessing fields using the pointer
	fmt.Println("Name:", personPointer.name) // Automatically dereferences
	fmt.Println("Age:", personPointer.age)

	// Modifying struct values using the pointer
	personPointer.age = 26
	fmt.Println("Updated struct:", p1)

	// Creating a pointer to a new instance of Person
	persPointer := new(Person)
	persPointer.name = "B"
	persPointer.age = 30

	fmt.Println("Struct created with new:", *persPointer)
}
