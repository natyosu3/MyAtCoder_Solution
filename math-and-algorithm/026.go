package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scan(&N)

	var cost float64 = 0.0
	for i := 1; i < N; i++ {
		cost += float64(N) / float64(i)
	}

	fmt.Printf("%.12f\n", cost)
}