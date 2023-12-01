package main

import "fmt"

func main() {
	tb := make([][]int, 9)

	for i := 0; i < 9; i++ {
		tb[i] = make([]int, 9)
		fmt.Scan(&tb[i][0], &tb[i][1], &tb[i][2], &tb[i][3], &tb[i][4], &tb[i][5], &tb[i][6], &tb[i][7], &tb[i][8])
	}

	var unique []int
	// 横
	for i := 0; i < 9; i++ {
		unique = uniqueElements(tb[i])
		if len(unique) != 9 {
			fmt.Println("No")
			return
		}
	}
	// 縦
	for i := 0; i < 9; i++ {
		var tmp []int
		for j := 0; j < 9; j++ {
			tmp = append(tmp, tb[j][i])
		}
		unique = uniqueElements(tmp)
		if len(unique) != 9 {
			fmt.Println("No")
			return
		}
	}

	// 3*3
	for i := 0; i < 9; i += 3 {
		for j := 0; j < 9; j += 3 {
			var tmp []int
			tmp = append(tmp, tb[i][j:j+3]...)
			tmp = append(tmp, tb[i+1][j:j+3]...)
			tmp = append(tmp, tb[i+2][j:j+3]...)
			unique = uniqueElements(tmp)
			if len(unique) != 9 {
				fmt.Println("No")
				return
			}
		}
	}
	fmt.Println("Yes")
}


func uniqueElements(slice []int) []int {
    set := make(map[int]struct{})
    for _, value := range slice {
        set[value] = struct{}{}
    }

    unique := make([]int, 0, len(set))
    for key := range set {
        unique = append(unique, key)
    }

    return unique
}