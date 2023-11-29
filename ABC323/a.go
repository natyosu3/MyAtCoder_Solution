package main

import (
	"fmt"
)

func main() {
	var S string

	fmt.Scan(&S)
	for i := 2; i <= 16; i +=2 {
		if string(S[i-1]) == "1" {
			fmt.Println("No")
			return
		}
	}
	fmt.Println("Yes")
}