// 654. Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/description/

package main

import (
	"fmt"
	"sort"
)

/*
    Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
1. The root is the maximum number in the array.
2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
*/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func constructMaximumBinaryTree(nums []int) *TreeNode {
	sort.Ints(nums)
	fmt.Println(nums)
	//
	//node := &TreeNode{Val: nums[len(nums)-1], Left: nil, Right: nil}
	//
	//for i := len(nums) - 1; i >= 0; i -= 2 {
	//	left := &TreeNode{Val: nums[i], Left: nil, Right: nil}
	//	right := &TreeNode{Val: nums[i], Left: nil, Right: nil}
	//
	//	node.Left = left
	//	node.Right = right
	//}

	return nil
}

func main() {
	constructMaximumBinaryTree([]int{2, 1, 4, 6, 11, 3, 5, 9})
}
