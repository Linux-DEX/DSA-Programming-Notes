package main

import ("fmt")

func main() {
  var myMap map[string]uint8 = make(map[string]uint8)
  fmt.Println(myMap)

  var myMap2 = map[string]uint8{"Adam": 23, "Sarah": 45}
  fmt.Println(myMap2["Adam"])
  fmt.Println(myMap2["Jason"]) // default value 0

  var age, ok = myMap2["Jason"]
  delete(myMap2, "Adam")
  if ok{
    fmt.Printf("The age is %v", age)
  } else {
    fmt.Printf("Invalid Name")
  }
}
