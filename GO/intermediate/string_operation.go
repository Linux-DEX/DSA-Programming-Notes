package main

import (
	"fmt"
	"strings"
)

func main() {
	// Trim functions
	s1 := "  @@Hello, Geeks!!  "
	s2 := "@@Hello, Geeks"
	result1 := strings.Trim(s2, "@!")
	fmt.Println(result1)

	result2 := strings.TrimRight(s2, "Geeks")
	fmt.Println(result2)

	result3 := strings.TrimSpace(s1)
	fmt.Println(result3)

	result4 := strings.TrimPrefix(s2, "@@")
	fmt.Println(result4)

	result5 := strings.TrimSuffix(s2, "eeks")
	fmt.Println(result5)

	// Split function
	s3 := "Welcome,to,ArchLinux"
	result6 := strings.Split(s3, ",")
	fmt.Println("Result:", result6)

	result7 := strings.SplitN(s3, ",", 2)
	fmt.Println("Result:", result7)

	result8 := strings.SplitAfterN(s3, ",", 2)
	fmt.Println("Result:", result8)

	// String Comparesion
	s4 := "Hello"
	s5 := "Geeks"
	s6 := "Hello"

	// Equality and inequality
	fmt.Println("s4 == s5:", s4 == s5) // false
	fmt.Println("s4 == s6:", s4 == s6) // true
	fmt.Println("s4 != s5:", s4 != s5) // true

	// Lexicographical comparison
	fmt.Println("s4 < s5:", s4 < s5)   // true
	fmt.Println("s4 > s5:", s4 > s5)   // false
	fmt.Println("s4 <= s6:", s4 <= s6) // true
	fmt.Println("s4 >= s6:", s4 >= s6) // true

	fmt.Println("strings.Compare(s4, s5):", strings.Compare(s4, s5)) // -1
	fmt.Println("strings.Compare(s4, s6):", strings.Compare(s4, s6)) // 0
	fmt.Println("strings.Compare(s5, s4):", strings.Compare(s5, s4)) // 1
}
