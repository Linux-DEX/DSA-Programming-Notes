package main

import "fmt"

// panic stops normal execution and starts unwinding the stack
// recover catches a panic - only works inside a deferred function
func safeDivide(a, b int) (result int, err error) {
	defer func() {
		if r := recover(); r != nil {
			err = fmt.Errorf("recovered from panic: %v", r)
		}
	}()

	if b == 0 {
		panic("division by zero")
	}
	return a / b, nil
}

func mustPositive(n int) {
	if n < 0 {
		panic(fmt.Sprintf("negative value: %d", n))
	}
	fmt.Println("value ok:", n)
}

func main() {
	// recover turns panic into a normal error
	res, err := safeDivide(10, 0)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Result:", res)
	}

	res, err = safeDivide(10, 2)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Result:", res)
	}

	// panic without recover will crash the program -
	// wrap risky calls when you need to keep running
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("caught in main:", r)
		}
	}()

	mustPositive(5)
	mustPositive(-1) // panics; recover in defer catches it, so process stays alive
	fmt.Println("this line does not run - panic aborts from the call site")
}
