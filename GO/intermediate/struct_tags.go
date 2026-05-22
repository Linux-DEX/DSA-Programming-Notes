package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type Book struct {
	Title     string `json:"title"`
	Author    string `json:"author"`
	PageCount int    `json:"pages"`
}

type Hidden struct {
	Visible string `json:"visible`
	Secret  string `json:"-"`
}

type Profile struct {
	Name  string `json:"name"`
	Email string `json:"email"`
}

func main() {
	fmt.Println("struct tags\n----")
	b := Book{
		Title:     "The Go Reader",
		Author:    "J. T. Hart",
		PageCount: 320,
	}
	out, _ := json.Marshal(b)
	fmt.Println(string(out))

	fmt.Println("\nHidden struct tags\n----")
	h := Hidden{Visible: "yes", Secret: "no"}
	json.NewEncoder(os.Stdout).Encode(h)

	fmt.Println("\nProfile struct tags\n----")
	data := []byte(`{"name":"Dana","email":"dana@example.com"}`)
	var p Profile
	err := json.Unmarshal(data, &p)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Printf("%+v\n", p)
}
