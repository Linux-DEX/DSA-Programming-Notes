package main

import "fmt"

// iota - auto-incrementing constant generator, resets per const block
const (
	Sunday = iota // 0
	Monday        // 1
	Tuesday       // 2
	Wednesday     // 3
	Thursday      // 4
	Friday        // 5
	Saturday      // 6
)

// iota with expressions
const (
	_  = iota             // skip 0
	KB = 1 << (10 * iota) // 1 << 10 = 1024
	MB                    // 1 << 20
	GB                    // 1 << 30
)

// custom type based on int (like an enum)
type Status int

const (
	StatusPending Status = iota
	StatusActive
	StatusDone
)

func (s Status) String() string {
	switch s {
	case StatusPending:
		return "pending"
	case StatusActive:
		return "active"
	case StatusDone:
		return "done"
	default:
		return "unknown"
	}
}

// type alias - new name for same type (interchangeable with int)
type ID = int

// defined type - distinct from int (needs conversion)
type Score int

func main() {
	fmt.Println("Tuesday:", Tuesday)
	fmt.Println("KB:", KB, "MB:", MB, "GB:", GB)

	st := StatusActive
	fmt.Println("status:", st, "value:", int(st))

	var id ID = 42
	var n int = id // alias: no conversion needed
	fmt.Println("id:", n)

	var sc Score = 99
	var raw int = int(sc) // defined type: must convert
	fmt.Println("score:", raw)
}
