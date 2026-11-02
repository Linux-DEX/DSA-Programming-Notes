package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"os"
	"strings"
)

// io.Reader / io.Writer are the core stream interfaces in Go
// anything that can Read bytes or Write bytes implements them

func main() {
	// strings.Reader implements io.Reader
	r := strings.NewReader("hello go")
	buf := make([]byte, 4)
	n, err := r.Read(buf)
	fmt.Println("read:", n, string(buf[:n]), "err:", err)

	// bytes.Buffer is both Reader and Writer
	var b bytes.Buffer
	b.WriteString("linux")
	b.WriteString("-dex")
	fmt.Println("buffer:", b.String())

	// io.Copy moves data from Reader to Writer
	var out bytes.Buffer
	io.Copy(&out, strings.NewReader("copied text"))
	fmt.Println("copy:", out.String())

	// write / read a temp file
	f, err := os.CreateTemp("", "go-notes-*.txt")
	if err != nil {
		fmt.Println("create error:", err)
		return
	}
	defer os.Remove(f.Name())
	defer f.Close()

	f.WriteString("line one\nline two\nline three\n")
	f.Seek(0, io.SeekStart)

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		fmt.Println("scan:", scanner.Text())
	}

	// os.ReadFile / os.WriteFile - whole file helpers
	path := f.Name()
	data, err := os.ReadFile(path)
	if err != nil {
		fmt.Println("ReadFile error:", err)
		return
	}
	fmt.Println("ReadFile:", string(data))
}
