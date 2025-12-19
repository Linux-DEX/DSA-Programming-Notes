package main

import (
	"fmt"
	"time"
)

func display(str string) {
	for i := 0; i < 3; i++ {
		time.Sleep(500 * time.Millisecond)
		fmt.Println(str)
	}
}

func task1(ch chan string) {
	time.Sleep(2 * time.Second)
	ch <- "Task 1 completed"
}

func task2(ch chan string) {
	time.Sleep(4 * time.Second)
	ch <- "Task 2 completed"
}

func portal1(channel1 chan string) {
	time.Sleep(3 * time.Second)
	channel1 <- "Welcome to channel 1"
}

func portal2(channel2 chan string) {
	time.Sleep(9 * time.Second)
	channel2 <- "Welcome to channel 2"
}

// For goroutine 1
func Aname() {

	arr1 := [4]string{"Rohit", "Suman", "Aman", "Ria"}

	for t1 := 0; t1 <= 3; t1++ {

		time.Sleep(150 * time.Millisecond)
		fmt.Printf("%s\n", arr1[t1])
	}
}

// For goroutine 2
func Aid() {

	arr2 := [4]int{300, 301, 302, 303}

	for t2 := 0; t2 <= 3; t2++ {

		time.Sleep(500 * time.Millisecond)
		fmt.Printf("%d\n", arr2[t2])
	}
}

func main() {
	go display("Hello, Goroutine!") // Runs concurrently
	display("Hello, Main!")

	// Anonymous Goroutine
	go func(s string) {
		for i := 0; i < 3; i++ {
			fmt.Println(s)
			time.Sleep(500 * time.Millisecond)
		}
	}("Hello from Anonymous Goroutine!")

	time.Sleep(2 * time.Second) // Allow Goroutine to finish
	fmt.Println("Main function complete.")

	// select statement
	ch1 := make(chan string)
	ch2 := make(chan string)

	go task1(ch1)
	go task2(ch2)

	select {
	case msg1 := <-ch1:
		fmt.Println(msg1)
	case msg2 := <-ch2:
		fmt.Println(msg2)
	}

	// basic blocking behavior
	ch := make(chan string)

	select {
	case msg := <-ch:
		fmt.Println(msg)
	default:
		fmt.Println("No channels are ready")
	}

	// handling multiple cases
	R1 := make(chan string)
	R2 := make(chan string)
	// calling function 1 and function 2 in goroutine
	go portal1(R1)
	go portal2(R2)
	select {
	// case 1 for portal 1
	case op1 := <-R1:
		fmt.Println(op1)
	// case 2 for portal 2
	case op2 := <-R2:
		fmt.Println(op2)
	}

	// using select with default case to avoid blocking
	chb1 := make(chan string)
	chb2 := make(chan string)

	select {
	case msg1 := <-chb1:
		fmt.Println(msg1)
	case msg2 := <-chb2:
		fmt.Println(msg2)
	default:
		fmt.Println("No tasks are ready yet")
	}

	// multiple goroutines
	fmt.Println("!...Main Go-routine Start...!")

	// calling Goroutine 1
	go Aname()

	// calling Goroutine 2
	go Aid()

	time.Sleep(3500 * time.Millisecond)
	fmt.Println("\n!...Main Go-routine End...!")
}

