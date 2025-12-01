package main

import "fmt"

func main() {

	linuxs := [4]string{"Arch", "Debian", "Gento", "Fedora"}
	fmt.Println("Elements of Array")
	for i := 0; i < 4; i++ {
		fmt.Println(linuxs[i])
	}

	arr := [3][3]string{{"C #", "C", "Python"}, {"Java", "Scala", "Perl"},
		{"C++", "Go", "HTML"}}

	// accessing the value of array
	fmt.Println("Elements of Array 1")
	for x := 0; x < 3; x++ {
		for y := 0; y < 3; y++ {

			fmt.Println(arr[x][y])
		}
	}

	var arr1 [2][2]int
	arr1[0][0] = 100
	arr1[0][1] = 200
	arr1[1][0] = 300
	arr1[1][1] = 400

	// Accessing the values of the array
	fmt.Println("Elements of array 2")
	for p := 0; p < 2; p++ {
		for q := 0; q < 2; q++ {
			fmt.Println(arr1[p][q])
		}
	}

	// Creating array
	// Using shorthand declaration
	arr2 := [3]int{9, 7, 6}
	arr3 := [...]int{9, 7, 6, 4, 5, 3, 2, 4}
	arr4 := [3]int{9, 3, 5}

	// Finding the length of the
	// array using len method
	fmt.Println("Length of the array 2 is:", len(arr2))
	fmt.Println("Length of the array 3 is:", len(arr3))
	fmt.Println("Length of the array 4 is:", len(arr4))
}
