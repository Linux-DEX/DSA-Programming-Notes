package main 

import ("fmt")

func main(){
  var p *int32 = new(int32)
  var i int32 
  fmt.Printf("The value p points to is: %v", *p)
  fmt.Printf("\nThe value if i is: %v", i)
  p = &i
  *p = 1 
  fmt.Printf("\nThe value p points to is: %v", *p)
  fmt.Printf("\nThe value of i address: %v", p)
  fmt.Printf("\nThe value if i is: %v", i)
}
