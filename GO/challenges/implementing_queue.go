package main

import (
	"errors"
	"fmt"
)

type Queue struct {
	Items []Flight
}

type Flight struct {
	Origin      string
	Destination string
	Price       int
}

// Implement
func (q *Queue) Pop() (Flight, error) {
	if q.IsEmpty() {
		return Flight{}, errors.New("Queue is Empty")
	} else {
		firstElemIndex := 0
		var flight Flight
		flight, q.Items = q.Items[firstElemIndex], q.Items[1:]
		return flight, nil
	}
}

// Implement
func (q *Queue) Push(f Flight) {
	q.Items = append(q.Items, f)
}

// Implement
func (q *Queue) Peek() (Flight, error) {
	if q.IsEmpty() {
		return Flight{}, errors.New("Queue is Empty")
	} else {
		return q.Items[0], nil
	}
}

func (q *Queue) IsEmpty() bool {
	if len(q.Items) == 0 {
		return true
	}
	return false
}

func main() {
	fmt.Println("Go Queue Implementation")

	q := Queue{}

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

	// Enqueue flights
	for _, flight := range flights {
		q.Push(flight)
		fmt.Println("Enqueued:", flight)
	}

	// Peek at front of queue
	frontFlight, err := q.Peek()
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Println("\nFront Flight:", frontFlight)

	// Dequeue all flights
	fmt.Println("\nDequeuing Flights:")
	for !q.IsEmpty() {
		flight, err := q.Pop()
		if err != nil {
			fmt.Println("Error:", err)
			break
		}

		fmt.Println("Dequeued:", flight)
	}
}
