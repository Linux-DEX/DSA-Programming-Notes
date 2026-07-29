package main

import "sync"

// ConcurrentBFSQueries concurrently processes BFS queries on the provided graph.
// - graph: adjacency list, e.g., graph[u] = []int{v1, v2, ...}
// - queries: a list of starting nodes for BFS.
// - numWorkers: how many goroutines can process BFS queries simultaneously.
//
// Return a map from the query (starting node) to the BFS order as a slice of nodes.
// YOU MUST use concurrency (goroutines + channels) to pass the performance tests.
// TODO: Implement concurrency-based BFS for multiple queries.
func ConcurrentBFSQueries(graph map[int][]int, queries []int, numWorkers int) map[int][]int {
	type Result struct {
		Query int
		Order []int
	}

	jobs := make(chan int)
	results := make(chan Result)

	var wg sync.WaitGroup

	// Worker function
	worker := func() {
		defer wg.Done()

		for start := range jobs {
			visited := make(map[int]bool)
			queue := []int{start}
			visited[start] = true

			var order []int

			for len(queue) > 0 {
				node := queue[0]
				queue = queue[1:]
				order = append(order, node)

				for _, neighbor := range graph[node] {
					if !visited[neighbor] {
						visited[neighbor] = true
						queue = append(queue, neighbor)
					}
				}
			}

			results <- Result{
				Query: start,
				Order: order,
			}
		}
	}

	// Start workers
	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go worker()
	}

	// Send jobs
	go func() {
		for _, q := range queries {
			jobs <- q
		}
		close(jobs)
	}()

	// Close results after workers finish
	go func() {
		wg.Wait()
		close(results)
	}()

	// Collect results
	answer := make(map[int][]int)
	for res := range results {
		answer[res.Query] = res.Order
	}

	return answer
}

// You can insert optional local tests here if desired.
func main() {
	graph := map[int][]int{
		0: {1, 2},
		1: {3, 4},
		2: {5},
		3: {},
		4: {5},
		5: {},
	}

	queries := []int{0, 1, 2}

	result := ConcurrentBFSQueries(graph, queries, 2)

	for start, order := range result {
		print("BFS from ", start, ": ")
		for _, node := range order {
			print(node, " ")
		}
		println()
	}
}
