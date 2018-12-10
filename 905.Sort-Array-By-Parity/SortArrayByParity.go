// 905. Sort Array By Parity
// https://leetcode.com/problems/sort-array-by-parity/

package main

func sortArrayByParity(A []int) []int {
	b := make([]int, len(A))
	s := 0
	e := len(A) - 1

	for _, v := range A {
		if v%2 == 0 {
			b[s] = v
			s += 1
		} else {
			b[e] = v
			e -= 1
		}
	}
	return b
}
