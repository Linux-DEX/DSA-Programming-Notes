package main

import (
	"errors"
	"fmt"
)

// checkNumber function checks if a number is positive or negative.
// If the number is negative, it returns an error.
func checkNumber(num int) (string, error) {
	if num < 0 {
		// Return an error when the number is negative
		return "", errors.New("number is negative")
	}
	// Return a success message if the number is positive
	return "number is positive", nil
}

// Declaring a custom error for invalid input
var ErrInvalidInput = errors.New("invalid input")

// Function to validate input and return an error if the input is empty
func validateInput(input string) error {
	if input == "" {
		// wrapping the custom error using fmt.Errorf and %w for proper error chaining
		return fmt.Errorf("validation error: %w", ErrInvalidInput)
	}
	return nil // No error if the input is valid
}

// CustomError defines a custom error type with a code and message.
type CustomError struct {
	Code    int
	Message string
}

// Error implements the error interface for CustomError
func (e *CustomError) Error() string {
	return fmt.Sprintf("Error %d: %s", e.Code, e.Message)
}

// generateError creates and returns a new CustomError
func generateError() error {
	return &CustomError{Code: 404, Message: "Resource not found"}
}

func main() {
	// Calling checkNumber with negative value (-5)
	result, err := checkNumber(-5)

	if err != nil {
		// if an error is returned, print the error message
		fmt.Println("Error:", err)
	} else {
		// if no error, print the success message
		fmt.Println(result)
	}

	// # Comparing Errors with errors.Is
	// Calling validateInput with an empty string to simulate an error
	err2 := validateInput("")

	// checking if the returned error matches the custom error using errors.Is()
	if errors.Is(err2, ErrInvalidInput) {
		fmt.Println("Detected invalid input") // Prints message if error is of type ErrInvalidInput
	}

	// # Custom Erros
	err3 := generateError()
	fmt.Println(err3)
}
