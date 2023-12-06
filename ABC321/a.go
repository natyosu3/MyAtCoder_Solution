package main

import (
	"fmt"
)

func main() {
	var N string

	fmt.Scan(&N)

	if len(N) == 1 {
		fmt.Println("Yes")
		return
	}

	for i := 0; i < len(N) - 1; i++ {
		tmp := int(N[i])
		if tmp <= int(N[i + 1]) {
			fmt.Println("No")
			return
		}
	}

	fmt.Println("Yes")
}