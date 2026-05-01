package main

import (
	"fmt"
	"sync"
)

func runner1(wg *sync.WaitGroup) {
	defer wg.Done() // decrease the wait group counter by 1
	fmt.Println("\nI am first runner")
}

func runner2(wg *sync.WaitGroup) {
	defer wg.Done() // decrease the wait group counter by 1
	fmt.Println("\nI am second runner")
}

func execute() {
	// create a wait group
	wg := new(sync.WaitGroup)
	wg.Add(2) // set the wait group counter to 2
	
	// we are incrementing the wait group counter because we have 2 goroutines
	go runner1(wg)
	go runner2(wg)

	// blocking call to wait for the wait group counter to reach 0
	wg.Wait()
}

func main() {
	// launch both runners
	execute()
}
