package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	// Creating and initializing a variable with a string Using shorthand declaration
	my_value_1 := "Welcome to Linux"

	var my_value_2 string
	my_value_2 = "Linux"

	fmt.Println("string 1: ", my_value_1)
	fmt.Println("string 2: ", my_value_2)

	// Creating and initializing a string using shorthand declaration
	mystr := "Welcome to Linux-DEX"

	fmt.Println("String:", mystr)
	/* if you trying to change
	      the value of the string
	      then the compiler will
	      throw an error, i.e,
	     cannot assign to mystr[1]

	   mystr[1]= 'G'
	   fmt.Println("String:", mystr)
	*/

	// string as a range in the for loop
	for index, s := range "Linux-DEX" {
		fmt.Printf("The index number of %c is %d\n", s, index)
	}

	// creating and initializing a string
	str := "welcome to linux-dex"

	// accessing the bytes of the given sring
	for c := 0; c < len(str); c++ {
		fmt.Printf("\nCharacter = %c Bytes = %x", str[c], str[c])
	}

	// Creating and initializing a slice of byte
	myslice1 := []byte{0x6c, 0x69, 0x6e, 0x75, 0x78}

	// Creating a string from the slice
	mystring1 := string(myslice1)

	// Displaying the string
	fmt.Println("\nString 1: ", mystring1)

	// Creating and initializing a slice of rune
	myslice2 := []rune{0x006c, 0x0069, 0x006e, 0x0075, 0x0078}

	// Creating a string from the slice
	mystring2 := string(myslice2)

	// Displaying the string
	fmt.Println("String 2: ", mystring2)

	// Creating and initializing a string using shorthand declaration
	mystrs := "Welcome to Linux-DEX!!"

	// Finding the length of the string Using len() function
	length1 := len(mystrs)

	// Using RuneCountInString() function
	length2 := utf8.RuneCountInString(mystrs)

	// Displaying the length of the string
	fmt.Println("string:", mystrs)
	fmt.Println("Length 1:", length1)
	fmt.Println("Length 2:", length2)
}
