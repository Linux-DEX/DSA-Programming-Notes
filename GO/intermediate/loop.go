package main

import (
	"fmt"
)

func main() {
	// simple for loop
	for i := 0; i < 4; i++ {
		fmt.Printf("Linux-DEX : %d\n", i)
	}

	// for loop as infinite loop
	// for {
	// 	fmt.Printf("linuxdex...\n")
	// }

	// for loop as while loop
	i := 0
	for i < 3 {
		i += 2
	}
	fmt.Println(i)

	// simple range in for loop
	distro := []string{"Arch", "Debian", "Gento", "Mint"}
	for i, j := range distro {
		fmt.Println(i, j)
	}

	// using loop for string
	for i, j := range "Linux-DEX" {
		fmt.Printf("The index number of %U is %d\n", j, i)
	}

	// for Map
	mdistro := map[int]string{
		22: "Arch",
		33: "Debian",
		44: "Gento",
	}
	for key, value := range mdistro {
		fmt.Println(key, value)
	}

	// for channel
	chnl := make(chan int)
	go func() {
		chnl <- 100
		chnl <- 1000
		chnl <- 10000
		chnl <- 100000
		close(chnl)
	}()
	for i := range chnl {
		fmt.Println(i)
	}
}
