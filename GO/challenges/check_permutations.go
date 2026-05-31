package main

import "fmt"

// implement me
func CheckPermutations(str1, str2 string) bool {
	if len(str1) != len(str2) {
		return false
	}

	counts := make(map[rune]int)

	for _, char := range str1 {
		counts[char]++
	}

	for _, char := range str2 {
		counts[char]--
		if counts[char] < 0 {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println("Check Permutations Challenge")

	str1 := "adcme"
	str2 := "medac"

	isPermutation := CheckPermutations(str1, str2)
	fmt.Println(isPermutation)
}
