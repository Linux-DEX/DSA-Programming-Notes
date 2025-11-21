package main

import "fmt"

func main() {
	// expression switch
	switch day := 2; day {
	case 1:
		fmt.Println("Monday")
	case 2:
		fmt.Println("Tuesday")
	case 3:
		fmt.Println("Wednesday")
	case 4:
		fmt.Println("Thursday")
	case 5:
		fmt.Println("Friday")
	default:
		fmt.Println("Invalid day")
	}

	// type switch
	var day interface{} = 3
	switch v := day.(type) {
	case int:
		switch v {
		case 1:
			fmt.Println("Monday")
		case 2:
			fmt.Println("Tuesday")
		case 3:
			fmt.Println("Wednesday")
		case 4:
			fmt.Println("Thursday")
		case 5:
			fmt.Println("Friday")
		default:
			fmt.Println("Invalid day")
		}
	default:
		fmt.Printf("Unknown type: %T\n", v)
	}

	// optional expression
	oday := 5

	switch {
	case oday == 1:
		fmt.Println("Monday")
	case oday == 4:
		fmt.Println("Thursday")
	case oday > 5:
		fmt.Println("Weekend")
	default:
		fmt.Println("Invalid day")
	}
}
