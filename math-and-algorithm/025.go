package main

import "fmt"
import "bufio"
import "os"
import "strings"
import "strconv"

func main() {
    var N int
    var ans float32 = 0.0
    fmt.Scanln(&N)

    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()
    A := make([]int, N)
    B := make([]int, N)

    inp := strings.Split(sc.Text(), " ")
    for index, val := range inp {
        A[index], _ = strconv.Atoi(val)
    }

    sc.Scan()
    inp = strings.Split(sc.Text(), " ")
    for index, val := range inp {
        B[index], _ = strconv.Atoi(val)
    }

    for i := 0; i < N; i++ {
        ans += (float32(A[i]) / 3.0) + (2.0*float32(B[i]) / 3.0) 
    }
    fmt.Println(ans)
}