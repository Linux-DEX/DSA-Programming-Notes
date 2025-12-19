package main

import "fmt"

func myfunc(ch chan int) {
	fmt.Println(234 + <-ch)
}

// Function
func myanotherfun(mychnl chan string) {

	for v := 0; v < 4; v++ {
		mychnl <- "Linux-DEX"
	}
	close(mychnl)
}
func main() {

	// Creating a channel using var keyword
	var mychannel chan int
	fmt.Println("Value of the channel: ", mychannel)
	fmt.Printf("Type of the channel: %T ", mychannel)

	// Creating a channel using make() function
	mychannel1 := make(chan int)
	fmt.Println("\nValue of the channel1: ", mychannel1)
	fmt.Printf("Type of the channel1: %T ", mychannel1)

	// send and receive data from a channel
	fmt.Println("start Main method")
	// Creating a channel
	ch := make(chan int)

	go myfunc(ch)
	ch <- 23
	fmt.Println("End Main method")

	// closing a channel
	// Creating a channel
	c := make(chan string)

	// calling Goroutine
	go myanotherfun(c)

	// When the value of ok is
	// set to true means the
	// channel is open and it
	// can send or receive data
	// When the value of ok is set to
	// false means the channel is closed
	for {
		res, ok := <-c
		if ok == false {
			fmt.Println("Channel Close ", ok)
			break
		}
		fmt.Println("Channel Open ", res, ok)
	}
}
