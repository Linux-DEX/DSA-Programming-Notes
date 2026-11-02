package main

import "fmt"

// Go favors composition over inheritance via embedding

type Address struct {
	City  string
	State string
}

func (a Address) Location() string {
	return a.City + ", " + a.State
}

type Person struct {
	Name string
	Age  int
	Address // embedded - fields/methods are promoted
}

type Employee struct {
	Person // embed Person (which embeds Address)
	Role   string
}

// interface embedding
type Reader interface {
	Read() string
}

type Writer interface {
	Write(data string)
}

type ReadWriter interface {
	Reader
	Writer
}

type Notebook struct {
	content string
}

func (n *Notebook) Read() string {
	return n.content
}

func (n *Notebook) Write(data string) {
	n.content = data
}

func main() {
	e := Employee{
		Person: Person{
			Name:    "Alex",
			Age:     28,
			Address: Address{City: "Pune", State: "MH"},
		},
		Role: "Dev",
	}

	// promoted fields - no need for e.Person.Name / e.Person.Address.City
	fmt.Println("Name:", e.Name)
	fmt.Println("City:", e.City)
	fmt.Println("Role:", e.Role)

	// promoted method from Address
	fmt.Println("Location:", e.Location())

	// still can access the inner struct explicitly
	fmt.Println("Person:", e.Person.Name)

	var rw ReadWriter = &Notebook{}
	rw.Write("go notes")
	fmt.Println("Notebook:", rw.Read())
}
