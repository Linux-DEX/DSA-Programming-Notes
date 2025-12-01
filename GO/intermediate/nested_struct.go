package main

import (
	"fmt"
)

type Address struct {
	Street     string
	City       string
	State      string
	PostalCode string
}

type Person struct {
	FirstName string
	LastName  string
	Age       int
	Address   Address
}

func main() {
	p := Person{
		FirstName: "John",
		LastName:  "Doe",
		Age:       30,
		Address: Address{
			Street:     "123 Main St",
			City:       "Anytown",
			State:      "CA",
			PostalCode: "12345",
		},
	}

	fmt.Println(p.FirstName, p.LastName)
	fmt.Println("Age:", p.Age)
	fmt.Println("Address:")
	fmt.Println("Street:", p.Address.Street)
	fmt.Println("City:", p.Address.City)
	fmt.Println("State:", p.Address.State)
	fmt.Println("Postal Code:", p.Address.PostalCode)
}
