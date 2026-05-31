package main

import (
	"cmp"
	"fmt"
	"slices"
)

// Flight - a struct that
// contains information about flights
type Flight struct {
	Origin      string
	Destination string
	Price       int
}

// SortByPrice sorts flights from highest to lowest
// implement SortByPrice()
func SortByPrice(flights []Flight) []Flight {
	slices.SortFunc(flights, func(a, b Flight) int {
		return cmp.Compare(b.Price, a.Price)
	})
	return flights
}

func printFlights(flights []Flight) {
	for _, flight := range flights {
		fmt.Printf("Origin: %s, Destination: %s, Price: %d\n", flight.Origin, flight.Destination, flight.Price)
	}
}

func main() {
	// an empty slice of flights
	flights := []Flight{
		{
			Origin:      "New York",
			Destination: "London",
			Price:       1200,
		},
		{
			Origin:      "Paris",
			Destination: "Tokyo",
			Price:       1500,
		},
		{
			Origin:      "Delhi",
			Destination: "Dubai",
			Price:       500,
		},
	}

	sortedList := SortByPrice(flights)
	printFlights(sortedList)
}
