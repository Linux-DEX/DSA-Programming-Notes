package main

import (
	"fmt"
	"sort"
)

func main() {
	array := [5]int{1, 2, 3, 4, 5}
	slice := array[1:4]

	fmt.Println("Array: ", array)
	fmt.Println("Slice: ", slice)

	slices := []int{1, 2, 3}
	slices = append(slices, 4, 5, 6)
	fmt.Println("Slices: ", slices)

	// Creating an array
	arr := [7]string{"This", "is", "the", "tutorial",
		"of", "Go", "language"}

	// Display array
	fmt.Println("Array:", arr)

	// Creating a slice
	myslice := arr[1:6]

	// Display slice
	fmt.Println("Slice:", myslice)

	// Display length of the slice
	fmt.Printf("Length of the slice: %d", len(myslice))

	// Display the capacity of the slice
	fmt.Printf("\nCapacity of the slice: %d", cap(myslice))

	// Creating a slice using the var keyword
	var my_slice_1 = []string{"Geeks", "for", "Geeks"}

	fmt.Println("My Slice 1:", my_slice_1)

	// Creating a slice using shorthand declaration
	my_slice_2 := []int{12, 45, 67, 56, 43, 34, 45}
	fmt.Println("My Slice 2:", my_slice_2)

	// creating slice from the given array
	my_arr := []string{"Arch", "Debian", "Fedora", "gento"}
	var my_slice_3 = my_arr[1:2]
	my_slice_4 := my_arr[0:]
	my_slice_5 := my_arr[:2]
	my_slice_6 := my_arr[:]

	fmt.Println("My Array: ", my_arr)
	fmt.Println("My Slice 3: ", my_slice_3)
	fmt.Println("My Slice 4: ", my_slice_4)
	fmt.Println("My Slice 5: ", my_slice_5)
	fmt.Println("My Slice 6: ", my_slice_6)

	// Creating an array of size 7 and slice this array  till 4 and return the reference of the slice Using make function
	var my_slice_7 = make([]int, 4, 7)
	fmt.Printf("Slice 1 = %v, \nlength = %d, \ncapacity = %d\n",
		my_slice_7, len(my_slice_7), cap(my_slice_7))

	// Creating another array of size 7 and return the reference of the slice Using make function
	var my_slice_8 = make([]int, 7)
	fmt.Printf("Slice 2 = %v, \nlength = %d, \ncapacity = %d\n",
		my_slice_8, len(my_slice_8), cap(my_slice_8))

	// Creating a slice
	my_slice := []string{"This", "is", "the", "tutorial", "of", "Go", "language"}

	// Iterate using for loop
	for e := 0; e < len(my_slice); e++ {
		fmt.Println(my_slice[e])
	}

	// Creating a zero value slice
	var myZeroSlice []string
	fmt.Printf("Length = %d\n", len(myZeroSlice))
	fmt.Printf("Capacity = %d ", cap(myZeroSlice))

	// Creating multi-dimensional slice
	s1 := [][]int{{12, 34},
		{56, 47},
		{29, 40},
		{46, 78},
	}

	// Accessing multi-dimensional slice
	fmt.Println("Slice s1 : ", s1)

	// Creating multi-dimensional slice
	s2 := [][]string{
		[]string{"Geeks", "for"},
		[]string{"Geeks", "GFG"},
		[]string{"gfg", "geek"},
	}

	// Accessing multi-dimensional slice
	fmt.Println("Slice s2 : ", s2)

	// Creating Slice
	slc1 := []string{"Python", "Java", "C#", "Go", "Ruby"}
	slc2 := []int{45, 67, 23, 90, 33, 21, 56, 78, 89}

	fmt.Println("Before sorting:")
	fmt.Println("Slice 1: ", slc1)
	fmt.Println("Slice 2: ", slc2)

	// Performing sort operation on the slice using sort function
	sort.Strings(slc1)
	sort.Ints(slc2)

	fmt.Println("\nAfter sorting:")
	fmt.Println("Slice 1: ", slc1)
	fmt.Println("Slice 2: ", slc2)
}
