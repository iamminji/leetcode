// 46. Permutations
// https://leetcode.com/problems/permutations/

package main

import (
	"fmt"
)

func subPermute(nums []int, left, right int, result *[][]int) {

	if left > right {
		*result = append(*result, nums)
		return
	}

	for i := left; i <= right; i++ {
		n := make([]int, len(nums))
		_ = copy(n, nums)
		n[left], n[i] = n[i], n[left]
		subPermute(n, left+1, right, result)
		n[left], n[i] = n[i], n[left]
	}
}

func permute(nums []int) [][]int {

	var result [][]int
	subPermute(nums, 0, len(nums)-1, &result)
	return result
}

func main() {
	nums := []int{1, 2, 3}
	fmt.Println(permute(nums))
}
