package main

import ("fmt")

func main() {
  // var intArr [3]int32
  // intArr[1] = 123
  // fmt.Println(intArr[0])
  // fmt.Println(intArr[1:3])
  //
  // fmt.Println(&intArr[0])
  // fmt.Println(&intArr[1])
  // fmt.Println(&intArr[2])

  // var intArr [3]int32 = [3]int32{1,2,3}
  intArr := [3]int32{1,2,3}
  fmt.Println(intArr)

  var intSlice []int32 = []int32{4,5,6}
  fmt.Printf("The length is %v with capacity %v", len(intSlice), cap(intSlice))
  intSlice = append(intSlice, 7)
  fmt.Printf("\nThe length is %v with capacity %v", len(intSlice), cap(intSlice))

  var intSlice2 []int32 = []int32{8,9}
  intSlice = append(intSlice, intSlice2...)
  fmt.Println("\n",intSlice)

  var intSlice3 []int32 = make(int32[], 3, 8) // 8 is the capacity, and 3 is lenght of slice
}

