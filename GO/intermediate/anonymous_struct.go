package main
import "fmt"

// Student struct with an anonymous structure and fields
type Student struct {
    struct {    // Anonymous inner structure for personal details
        name string
        enrollment int
    }
    GPA float64  // Standard field
}

func main() {
    student := Student{
        struct {
            name string
            enrollment int
        }{
            name: "A",
            enrollment: 12345,
        },
        GPA: 3.8,
    }
    fmt.Println("Name:", student.name)
    fmt.Println("Enrollment:", student.enrollment)
    fmt.Println("GPA:", student.GPA)
}

