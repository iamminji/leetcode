// 565. Array Nesting
// https://leetcode.com/problems/array-nesting/

package main

import (
	"fmt"
)

func arrayNesting(nums []int) int {
	res := make([]int, len(nums))
	visited := make([]bool, len(nums))

	i := 0

	for i < len(nums) {
		if visited[i] {
			i += 1
			continue
		}
		res[nums[i]] = res[i] + 1
		visited[i] = true
		i = nums[i]
	}

	result := 0
	for j := range res {
		result = func(n1, n2 int) int {
			if n1 > n2 {
				return n1
			}
			return n2
		}(result, res[j])
	}
	return result
}

func main() {
	fmt.Println(arrayNesting([]int{5, 4, 0, 3, 1, 6, 2}))
	fmt.Println(arrayNesting([]int{0, 1, 2, 3, 4, 5, 6}))
	fmt.Println(arrayNesting([]int{6, 5, 4, 3, 2, 1, 0}))
	fmt.Println(arrayNesting([]int{0, 2, 1}))
}
