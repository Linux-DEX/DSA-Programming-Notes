package main

import "fmt"

// Function to calculate the average of an array
func calculateAverage(arr [6]int, size int) int {
	var sum int
	for _, value := range arr {
		sum += value
	}
	return sum / size
}

// Function to increment each element of the array
func incrementArray(arr *[5]int) {
	for i := range arr {
		arr[i]++ // Increment each element by 1
	}
}

func main() {
	// copy array into another array
	var source = [5]int{10, 20, 30, 40, 50}

	var destination [5]int

	// Manually copying each element
	for i := 0; i < len(source); i++ {
		destination[i] = source[i]
	}

	fmt.Println("Source:", source)
	fmt.Println("Destination:", destination)

	// direct assignment
	var destination2 [5]int = source
	fmt.Println("Destination2:", destination2)

	// copy array using pointer
	var destination3 *[5]int = &source
	fmt.Println("Destination3:", destination3)

	// passing array to function
	scores := [6]int{67, 59, 29, 35, 4, 34}
	average := calculateAverage(scores, len(scores))
	fmt.Printf("%d\n", average)

	values := [5]int{1, 2, 3, 4, 5}

	// Modifying the array
	incrementArray(&values)

	fmt.Println("Incremented array:", values)
}
