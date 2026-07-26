package main

import (
	"fmt"
	"strings"
	"unicode"
)

// CountWordFrequency takes a string containing multiple words and returns
// a map where each key is a word and the value is the number of times that
// word appears in the string. The comparison is case-insensitive.
//
// Words are defined as sequences of letters and digits.
// All words are converted to lowercase before counting.
// All punctuation, spaces, and other non-alphanumeric characters are ignored.
//
// Example:
// Input: "The quick brown fox jumps over the lazy dog. The fox is quick."
// Output:
// map[string]int{
//     "the": 2,
//     "quick": 2,
//     "brown": 1,
//     "fox": 2,
//     "jumps": 1,
//     "over": 1,
//     "lazy": 1,
//     "dog": 1,
//     "is": 1,
// }

// TODO: Implement this method
func CountWordFrequency(text string) map[string]int {
	frequency := make(map[string]int)

	var word strings.Builder

	for _, char := range text {
		if unicode.IsLetter(char) || unicode.IsDigit(char) {
			word.WriteRune(unicode.ToLower(char))
		} else {
			if word.Len() > 0 {
				frequency[word.String()]++
				word.Reset()
			}
		}
	}

	if word.Len() > 0 {
		frequency[word.String()]++
	}

	return frequency
}

func main() {
	text := "The quick brown fox jumps over the lazy dog. The fox is quick."

	result := CountWordFrequency(text)

	fmt.Println(result)
}
