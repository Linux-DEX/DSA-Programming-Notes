package main

import (
	"fmt"
)

// defining a struct
type Person struct {
	name string
	age  int
}

// Creating a custom type based on int
type number int

// Defining a struct
type person struct {
	name string
}

// defining a method with struct receiver
func (p Person) display() {
	fmt.Println("Name:", p.name)
	fmt.Println("Age:", p.age)
}

// Defining a method with a non-struct receiver
func (n number) square() number {
	return n * n
}

// Method with pointer receiver to modify data
func (p *person) changeName(newName string) {
	p.name = newName
}

func main() {
	// Creating an instance of the struct
	a := Person{name: "a", age: 25}

	// calling the method
	a.display()

	b := number(4)
	c := b.square()

	fmt.Println("Square of", b, "is", c)

	d := person{name: "a"}

	fmt.Println("Before:", a.name)

	// Calling the method to change the name
	d.changeName("b")

	fmt.Println("After:", d.name)
}
