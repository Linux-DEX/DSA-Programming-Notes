package main

import ("fmt")

func main(){
  var myMap = map[string]uint8{"Admin": 23, "Sarah": 45}

  for name, age:= range myMap{
    fmt.Printf("Name: %v, Age: %v \n", name, age)
  }

  i := 0
  for i<10 {
    fmt.Println(i)
    i=i+1
  }

  var j int = 0 
  for {
    if j >= 10 {
      break
    }
    fmt.Println(j)
    j = j + 1
  }

  for i:=0; i<10; i++ {
    fmt.Println(i)
  }
}
