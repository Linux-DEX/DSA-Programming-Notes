package main

import (
	"errors"
	"fmt"
)

type Stack struct {
	Items []Flight
}

type Flight struct {
	Origin      string
	Destination string
	Price       int
}

// Implement
func (s *Stack) Pop() (Flight, error) {
	if s.IsEmpty() {
		return Flight{}, errors.New("Stack is Empty")
	} else {
		lastElemIndex := len(s.Items) - 1
		flight := s.Items[lastElemIndex]
		s.Items = s.Items[:lastElemIndex]
		return flight, nil
	}
}

// Implement
func (s *Stack) Push(f Flight) {
	s.Items = append(s.Items, f)
}

// Implement
func (s *Stack) Peek() (Flight, error) {
	if s.IsEmpty() {
		return Flight{}, errors.New("Stack is Empty")
	} else {
		lastElemIndex := len(s.Items) - 1
		flight := s.Items[lastElemIndex]
		return flight, nil
	}
}

func (s *Stack) IsEmpty() bool {
	if len(s.Items) == 0 {
		return true
	}

	return false
}

func main() {
	fmt.Println("Go Stack Implementation")
	s := Stack{}

	// Sample flight data
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

	for _, flight := range flights {
		s.Push(flight)
	}

	topFlight, err := s.Peek()
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Println("Top Flight:", topFlight)

	for !s.IsEmpty() {
		flight, err := s.Pop()
		if err != nil {
			fmt.Println("Error:", err)
			break
		}

		fmt.Println("Popped:", flight)
	}

}
