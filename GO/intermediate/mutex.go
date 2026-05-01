package main

import (
	"fmt"
	"sync"
)

var counter int

// this mutex will synchronize access to state
var mu sync.Mutex

// This is the function we’ll run in every goroutine. Note that a WaitGroup must be passed to functions by pointer.
func worker(wg *sync.WaitGroup) {
	// Lock() the mutex to ensure  exclusive access to the state,  increment the value, Unlock() the mutex
	mu.Lock()
	counter++
	mu.Unlock()
	// On return, notify the WaitGroup that we’re done.
	wg.Done()
}

func main() {
	// this waitgroup waits for all workers to finish
	var wg sync.WaitGroup

	// Launch several goroutines and increment the WaitGroup counter for each
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go worker(&wg)
	}

	// Block until the WaitGroup counter goes back to 0; all the workers notified they’re done.
	wg.Wait()
	fmt.Println("counter:", counter)
}
