package main

import (
	"errors"
	"fmt"
)

// run demos with:  go run testing_basics.go
// run tests with:  go test -v testing_basics.go testing_basics_test.go

func Add(a, b int) int {
	return a + b
}

func Divide(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("division by zero")
	}
	return a / b, nil
}

func main() {
	fmt.Println("Add:", Add(2, 3))

	res, err := Divide(10, 2)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Divide:", res)
	}
}
