// 55. Jump Game
// https://leetcode.com/problems/jump-game/

package main

import "fmt"

func jump(nums []int, i int, visited []bool) (result bool) {

	if visited[i] {
		return result
	}
	if i >= len(nums) {
		return false
	} else if i == len(nums)-1 {
		return true
	} else {
		visited[i] = true
		for j := 1; j <= nums[i]; j++ {
			result = result || jump(nums, i+j, visited)
		}
	}
	return result
}

func canJump(nums []int) bool {
	visited := make([]bool, len(nums))
	return jump(nums, 0, visited)
}

func main() {
	// true
	fmt.Println(canJump([]int{2, 3, 1, 1, 4}))
	// false
	fmt.Println(canJump([]int{3, 2, 1, 0, 4}))
}
