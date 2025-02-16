package main

import (
  "fmt"
  "strings"
)

func main() {
  // var myString = "resume"
  // var indexed = myString[0]
  // fmt.Printf("%v, %T\n", indexed, indexed)
  //
  // for i, v := range myString {
  //   fmt.Println(i, v)
  // }

  var myString = []rune("resume")
  var indexed = myString[0]
  fmt.Printf("%v, %T\n", indexed, indexed)

  for i, v := range myString {
    fmt.Println(i, v)
  }

  var myRune = 'a'
  fmt.Printf("\nmyRune = %v", myRune)

  // var strSlice = []string{"l", "i", "n", "u", "x","d","e","x"}
  // var catStr = ""
  // for i := range strSlice{
  //   catStr += strSlice[i]
  // }
  // fmt.Printf("\n%v", catStr)

  var strSlice = []string{"l", "i", "n", "u", "x","d","e","x"}
  var strBuilder strings.Builder
  for i := range strSlice{
    strBuilder.WriteString(strSlice[i])
  }
  catStr := strBuilder.String()
  fmt.Printf("\n%v", catStr)
}
