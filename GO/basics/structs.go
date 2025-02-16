package main

import (
	"fmt"
)

type gasEngine struct{
	mpg uint8
	gallons uint8
	ownerInfo owner
}

type owner struct {
	name string
}

func (e gasEngine) milesLeft() uint8 {
	return e.gallons*e.mpg
}

func main() {
	// var myEngine gasEngine = gasEngine{mpg: 25, gallons:15}
	var myEngine gasEngine = gasEngine{25, 15, owner{"Alex"}}
	myEngine.mpg = 20
	fmt.Println(myEngine.mpg, myEngine.gallons, myEngine.ownerInfo.name)

	// this is not re-useable
	// var myEngine2 = struct{
	// 	mpg uint8
	// 	gallons uint8
	// }{23, 13}

	fmt.Printf("Total miles left in tank: %v", myEngine.milesLeft())
}