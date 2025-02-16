package main
import (
    "fmt"
    "math"
)

type Shape interface {
    Area() float64
    Perimeter() float64
}

type Circle struct {
    radius float64
}

type Rectangle struct {
    length, width float64
}
func (c Circle) Area() float64 {
    return math.Pi * c.radius * c.radius
}

func (c Circle) Perimeter() float64 {
    return 2 * math.Pi * c.radius
}

func (r Rectangle) Area() float64 {
    return r.length * r.width
}

func (r Rectangle) Perimeter() float64 {
    return 2 * (r.length + r.width)
}

func main() {
    var s Shape

    s = Circle{radius: 5}
    fmt.Println("C Area:", s.Area())
    fmt.Println("C Perimeter:", s.Perimeter())

    s = Rectangle{length: 4, width: 3}
    fmt.Println("R Area:", s.Area())
    fmt.Println("R Perimeter:", s.Perimeter())
}
