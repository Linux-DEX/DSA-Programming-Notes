package main

import (
	"errors"
	"fmt"
)

var ErrNotFound = errors.New("not found")

type ValidationError struct {
	Field string
	Msg   string
}

func (e *ValidationError) Error() string {
	return fmt.Sprintf("%s: %s", e.Field, e.Msg)
}

func findUser(id int) error {
	if id <= 0 {
		return fmt.Errorf("findUser: %w", ErrNotFound)
	}
	return nil
}

func loadProfile(id int) error {
	err := findUser(id)
	if err != nil {
		// wrap again - keeps the chain for errors.Is / errors.As
		return fmt.Errorf("loadProfile: %w", err)
	}
	return nil
}

func validateAge(age int) error {
	if age < 0 {
		return &ValidationError{Field: "age", Msg: "must be >= 0"}
	}
	return nil
}

func register(age int) error {
	if err := validateAge(age); err != nil {
		return fmt.Errorf("register: %w", err)
	}
	return nil
}

func main() {
	// errors.Is - walk the wrap chain for sentinel errors
	err := loadProfile(-1)
	if errors.Is(err, ErrNotFound) {
		fmt.Println("Is NotFound:", err)
	}

	// errors.Unwrap - peel one layer
	fmt.Println("Unwrap once:", errors.Unwrap(err))

	// errors.As - extract a concrete error type from the chain
	err2 := register(-5)
	var ve *ValidationError
	if errors.As(err2, &ve) {
		fmt.Println("As ValidationError field:", ve.Field, "msg:", ve.Msg)
	}

	// %v prints message, %+v / just Error() still string -
	// use Is/As instead of string compare
	fmt.Println("full chain:", err2)
}
