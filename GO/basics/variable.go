package main

import "fmt"
import "unicode/utf8"

func main(){
	var intNum int = 31023 
	intNum = intNum + 1
	intNum += 1
	fmt.Println(intNum)

	var floatNum float32 = 123401.23
	fmt.Println(floatNum)

	var floatNum32 float32 = 10.1
	var intNum32 int32 = 2 
	var result float32 = floatNum32 + float32(intNum32)
	fmt.Println(result)

	var intNum1 int = 3
	var intNum2 int = 2 
	fmt.Println(intNum1/intNum2)
	fmt.Println(intNum1%intNum2)

	// var myString string = "hello world"
	var myString string = "hello" + " " + "world"
	// var myString string = `hello world`
	fmt.Println(myString)

	fmt.Println(len("test")) // this doesn't give lenght of string , it return byte of the string

	fmt.Println(utf8.RuneCountInString("linuxdex")) // give the length of character

	var myRune rune = 'a'
	fmt.Println(myRune)

	var myBoolean bool = false
	fmt.Println(myBoolean)

	// you can declare variable like this
	myVar := "text"
	fmt.Println(myVar)

	var1, var2 := 1, 2
	fmt.Println(var1, var2)

	const myConst string = "const value"
	fmt.Println(myConst)

	
}