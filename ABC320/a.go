package main

import (
	"fmt"
	"math"
)

func main() {
	var A, B  float64
	var ans int

	fmt.Scan(&A, &B)

	ans = int(math.Pow(A, B)) + int(math.Pow(B, A))

	fmt.Println(ans)
}