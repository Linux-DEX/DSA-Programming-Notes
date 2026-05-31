package main

import (
	"errors"
	"fmt"
)

type Flight struct {
	Origin      string
	Destination string
	Price       int
}

// Implement me
func GetMinMax(flights []Flight) (int, int, error) {
	if len(flights) == 0 {
		return 0, 0, errors.New("no flights available")
	}

	minPrice := flights[0].Price
	maxPrice := flights[0].Price

	for _, flight := range flights[1:] {
		if flight.Price < minPrice {
			minPrice = flight.Price
		}

		if flight.Price > maxPrice {
			maxPrice = flight.Price
		}
	}

	return minPrice, maxPrice, nil
}

func main() {
	fmt.Println("Getting the Minimum and Maximum Flight Prices")

	flights := []Flight{
		{
			Origin:      "New York",
			Destination: "London",
			Price:       750,
		},
		{
			Origin:      "Bangalore",
			Destination: "Singapore",
			Price:       320,
		},
		{
			Origin:      "Tokyo",
			Destination: "Sydney",
			Price:       680,
		},
		{
			Origin:      "Paris",
			Destination: "Rome",
			Price:       120,
		},
		{
			Origin:      "Dubai",
			Destination: "Mumbai",
			Price:       250,
		},
	}

	minPrice, maxPrice, err := GetMinMax(flights)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Printf("Minimum Flight Price: %d\n", minPrice)
	fmt.Printf("Maximum Flight Price: %d\n", maxPrice)
}
