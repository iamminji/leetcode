// 977. Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/

package main

import (
	"fmt"
	"sort"
)

func sortedSquares(A []int) []int {

	res := make([]int, 0)
	for _, num := range A {
		res = append(res, num*num)
	}

	sort.Ints(res)
	return res
}

func main() {
	fmt.Println(sortedSquares([]int{-4, -1, 0, 3, 10}))
}
