package main

import (
  "fmt"
)

type Developer struct {
  Name string
  Age int
}

// Implement GetDeveloper func
func GetDeveloper(name interface{}, age interface{}) Developer {
  dev := Developer{Name: name.(string), Age: age.(int)}
  return dev
}

func main() {
  fmt.Println("Hello World")

  var name interface{} = "Elliot"
  var age interface{} = 26

  dynamicDev := GetDeveloper(name, age)
  fmt.Println(dynamicDev.Name)
}

