package main

import (
	"fmt"
)

const PI = 3.14
const s string = "linux-dex"

func main() {
	const dex = "linuxdex"
	fmt.Println("hello :", dex)
	fmt.Println("Happy", PI, "Day")

	const Correct = true
	fmt.Println("Go rules?", Correct)
	fmt.Println("constent string s:", s)
}
