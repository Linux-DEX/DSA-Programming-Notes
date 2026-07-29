package main

import (
	"fmt"
)

func main() {
	// Standard U.S. coin denominations in cents
	denominations := []int{1, 5, 10, 25, 50}

	// Test amounts
	amounts := []int{87, 42, 99, 33, 7}

	for _, amount := range amounts {
		// Find minimum number of coins
		minCoins := MinCoins(amount, denominations)

		// Find coin combination
		coinCombo := CoinCombination(amount, denominations)

		// Print results
		fmt.Printf("Amount: %d cents\n", amount)
		fmt.Printf("Minimum coins needed: %d\n", minCoins)
		fmt.Printf("Coin combination: %v\n", coinCombo)
		fmt.Println("---------------------------")
	}
}

// TODO: Implement this function
// MinCoins returns the minimum number of coins needed to make the given amount.
// If the amount cannot be made with the given denominations, return -1.
func MinCoins(amount int, denominations []int) int {
	const INF = int(^uint(0) >> 1) // Max int

	dp := make([]int, amount+1)
	for i := 1; i <= amount; i++ {
		dp[i] = INF
	}

	dp[0] = 0

	for _, coin := range denominations {
		for i := coin; i <= amount; i++ {
			if dp[i-coin] != INF && dp[i-coin]+1 < dp[i] {
				dp[i] = dp[i-coin] + 1
			}
		}
	}

	if dp[amount] == INF {
		return -1
	}

	return dp[amount]
}

// TODO: Implement this function
// CoinCombination returns a map with the specific combination of coins that gives
// the minimum number. The keys are coin denominations and values are the number of
// coins used for each denomination.
// If the amount cannot be made with the given denominations, return an empty map.
func CoinCombination(amount int, denominations []int) map[int]int {
	const INF = int(^uint(0) >> 1)

	dp := make([]int, amount+1)
	lastCoin := make([]int, amount+1)

	for i := 1; i <= amount; i++ {
		dp[i] = INF
		lastCoin[i] = -1
	}

	dp[0] = 0

	for _, coin := range denominations {
		for i := coin; i <= amount; i++ {
			if dp[i-coin] != INF && dp[i-coin]+1 < dp[i] {
				dp[i] = dp[i-coin] + 1
				lastCoin[i] = coin
			}
		}
	}

	if dp[amount] == INF {
		return map[int]int{}
	}

	result := make(map[int]int)
	for amount > 0 {
		coin := lastCoin[amount]
		result[coin]++
		amount -= coin
	}

	return result
}
