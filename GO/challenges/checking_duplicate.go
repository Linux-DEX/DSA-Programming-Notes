package main

import "fmt"

type Developer struct {
	Name string
	Age  int
}

// Implement FilterUnique()
func FilterUnique(developers []Developer) []string {
	seen := make(map[string]bool)
	var result []string

	for _, dev := range developers {
		if !seen[dev.Name] {
			seen[dev.Name] = true
			result = append(result, dev.Name)
		}
	}

	return result
}

func main() {
	developers := []Developer{
		{Name: "Alice", Age: 25},
		{Name: "Bob", Age: 30},
		{Name: "Alice", Age: 28},
		{Name: "Charlie", Age: 35},
		{Name: "Bob", Age: 32},
	}

	fmt.Println("Developers:", developers)

	result := FilterUnique(developers)
	fmt.Println("Unique Names:", result)
}
