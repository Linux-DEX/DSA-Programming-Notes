package main

import (
	"fmt"
	"maps"
)

func main() {
	ages := map[string]int{
		"A": 30,
		"B": 25,
		"C": 35,
	}

	// retrieving values
	bAge := ages["B"]

	fmt.Println("B's age:", bAge)

	// adding key-value pair
	ages["D"] = 32

	// iterating over a map
	for key, value := range ages {
		fmt.Println(key, value)
	}

	// checking key existence
	if eAge, ok := ages["E"]; ok {
		fmt.Println("key exists", eAge)
	} else {
		fmt.Println("key does not exists")
	}

	m := make(map[string]int)
	m["k1"] = 7
	m["k2"] = 13

	v1 := m["k1"]
	fmt.Println("v1:", v1)

	v3 := m["k2"]
	fmt.Println("v3:", v3)

	fmt.Println("len:", len(m))

	// deleting key
	delete(m, "k2")
	fmt.Println("map :", m)

	// clearing map
	clear(m)
	fmt.Println("map :", m)

	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)

	n2 := map[string]int{"foo": 1, "bar": 2}
	// checking map are equal
	if maps.Equal(n, n2) {
		fmt.Println("n == n2")
	}
}
