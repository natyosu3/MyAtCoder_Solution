package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scanln(&N)
	res := make([]string, N)
	win_ct := make([]int, N)

	for i := 0; i < N; i++ {
		fmt.Scanln(&res[i])
	}

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if res[i][j] == 'o' {
				win_ct[i]++
			}
		}
	}

	indexes := make([]int, N)
	for i := 0; i < N; i++ {
		indexes[i] = i
	}
	sort.SliceStable(indexes, func(i, j int) bool {
		if win_ct[indexes[i]] == win_ct[indexes[j]] {
			return indexes[i] < indexes[j]
		}
		return win_ct[indexes[i]] > win_ct[indexes[j]]
	})

	for _, index := range indexes {
		fmt.Print(index + 1, " ")
	}
}