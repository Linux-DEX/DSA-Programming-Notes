package main

import (
	"context"
	"fmt"
	"time"
)

// context carries deadlines, cancellation signals, and request-scoped values
// always pass as first argument: func Do(ctx context.Context, ...)

func work(ctx context.Context, name string) {
	for i := 1; i <= 5; i++ {
		select {
		case <-ctx.Done():
			fmt.Println(name, "stopped:", ctx.Err())
			return
		default:
			fmt.Println(name, "step", i)
			time.Sleep(200 * time.Millisecond)
		}
	}
	fmt.Println(name, "finished")
}

func fetch(ctx context.Context) (string, error) {
	select {
	case <-time.After(500 * time.Millisecond):
		return "data", nil
	case <-ctx.Done():
		return "", ctx.Err()
	}
}

func main() {
	// WithCancel - manual cancel
	ctx1, cancel1 := context.WithCancel(context.Background())
	go work(ctx1, "worker-A")
	time.Sleep(450 * time.Millisecond)
	cancel1()
	time.Sleep(100 * time.Millisecond)

	// WithTimeout - auto cancel after duration
	ctx2, cancel2 := context.WithTimeout(context.Background(), 300*time.Millisecond)
	defer cancel2()

	result, err := fetch(ctx2)
	if err != nil {
		fmt.Println("fetch error:", err)
	} else {
		fmt.Println("fetch result:", result)
	}

	// WithDeadline - cancel at a specific time
	deadline := time.Now().Add(150 * time.Millisecond)
	ctx3, cancel3 := context.WithDeadline(context.Background(), deadline)
	defer cancel3()
	go work(ctx3, "worker-B")
	time.Sleep(300 * time.Millisecond)

	// WithValue - request-scoped data (use sparingly)
	ctx4 := context.WithValue(context.Background(), "reqID", "abc-123")
	fmt.Println("reqID:", ctx4.Value("reqID"))
}
