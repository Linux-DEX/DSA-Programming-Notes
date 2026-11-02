package main

import (
	"fmt"
	m "math" // import alias
)

/*
Packages & Modules
------------------
- Every Go file starts with `package <name>`
- `package main` = executable; other names = libraries
- Module = a collection of packages, defined by go.mod at the repo root

  go mod init github.com/you/project
  go get <dependency>
  go mod tidy

Visibility (export rules):
- Name starts with Uppercase  -> exported (public outside package)
- Name starts with lowercase  -> unexported (package-private only)
*/

// Exported - visible to other packages
func Add(a, b int) int {
	return a + b
}

// unexported - only usable inside this package
func hiddenHelper(msg string) string {
	return "internal: " + msg
}

// Exported type
type User struct {
	Name string // exported field
	age  int    // unexported field
}

func (u User) Greet() string {
	return fmt.Sprintf("Hi, %s", u.Name)
}

func (u User) years() int {
	return u.age
}

func main() {
	fmt.Println("Add:", Add(2, 3))
	fmt.Println(hiddenHelper("ok"))

	u := User{Name: "Alex", age: 25}
	fmt.Println(u.Greet())
	fmt.Println("age via method:", u.years())

	// import alias in action
	fmt.Println("Pi via alias:", m.Pi)

	/*
		Typical layout:
		  myapp/
		    go.mod
		    cmd/myapp/main.go     // package main
		    internal/auth/auth.go // not importable outside module
		    pkg/util/util.go      // reusable library package
	*/
}
