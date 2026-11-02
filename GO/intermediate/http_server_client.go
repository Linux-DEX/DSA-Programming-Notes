package main

import (
	"fmt"
	"io"
	"net/http"
	"net/http/httptest"
	"strings"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	fmt.Fprint(w, "hello")
}

func echoHandler(w http.ResponseWriter, r *http.Request) {
	body, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad body", http.StatusBadRequest)
		return
	}
	defer r.Body.Close()
	w.Header().Set("Content-Type", "text/plain")
	w.Write(body)
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/hello", helloHandler)
	mux.HandleFunc("/echo", echoHandler)

	// httptest.NewServer - local server for demos (no hang)
	ts := httptest.NewServer(mux)
	defer ts.Close()

	// client GET
	resp, err := http.Get(ts.URL + "/hello")
	if err != nil {
		fmt.Println("GET error:", err)
		return
	}
	defer resp.Body.Close()
	data, _ := io.ReadAll(resp.Body)
	fmt.Println("GET status:", resp.StatusCode, "body:", string(data))

	// client POST
	resp2, err := http.Post(ts.URL+"/echo", "text/plain", strings.NewReader("ping"))
	if err != nil {
		fmt.Println("POST error:", err)
		return
	}
	defer resp2.Body.Close()
	data2, _ := io.ReadAll(resp2.Body)
	fmt.Println("POST status:", resp2.StatusCode, "body:", string(data2))

	// httptest recorder - unit-test style, no real network
	req := httptest.NewRequest(http.MethodGet, "/hello", nil)
	rr := httptest.NewRecorder()
	helloHandler(rr, req)
	fmt.Println("recorder:", rr.Code, rr.Body.String())
}
