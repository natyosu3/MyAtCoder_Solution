package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)

	var N int
	fmt.Scanln(&N)

	P := make([]int, N)
	Q := make([]int, N)

	for i := 0; i < N; i++ {
		sc.Scan()
		tmp := strings.Split(sc.Text(), " ")
		P[i], _ = strconv.Atoi(tmp[0])
		Q[i], _ = strconv.Atoi(tmp[1])
	}

	var exp float64

	for i := 0; i < N; i++ {
		exp += 1 / float64(P[i]) * float64(Q[i])
	}

	fmt.Println(exp)
}